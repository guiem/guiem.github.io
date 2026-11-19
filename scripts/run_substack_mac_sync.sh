#!/usr/bin/env bash
# Run from macOS (manually or with launchd). Propose Substack imports as a PR.
# This script NEVER writes to master, merges, or publishes a post.
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"
REPO="guiem/guiem.github.io"
BASE="master"
SYNC_BRANCH="automation/substack-converses-mac"
DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then DRY_RUN=true; elif [[ $# -gt 0 ]]; then echo "Usage: $0 [--dry-run]" >&2; exit 2; fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${ROOT}/.venv-substack/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  echo "Missing Python environment. Run: bash scripts/install_substack_mac_sync.sh" >&2
  exit 1
fi
for binary in git gh curl; do
  command -v "$binary" >/dev/null || { echo "Missing prerequisite: $binary" >&2; exit 1; }
done
gh auth status >/dev/null 2>&1 || {
  echo "GitHub CLI not authenticated. Run 'gh auth login' and 'gh auth setup-git'." >&2
  exit 1
}

WORK="$(mktemp -d "${TMPDIR:-/tmp}/converses-substack.XXXXXXXX")"
trap 'rm -rf "$WORK"' EXIT
echo "Cloning $REPO into a temporary directory..."
gh repo clone "$REPO" "$WORK/repo" -- --quiet
cd "$WORK/repo"
git fetch --quiet origin "$BASE"
git config user.name "Converses de casa sync"
git config user.email "substack-sync@users.noreply.github.com"

# Reuse an open sync branch without force-pushing. Merge changes from master;
# fail safely if the user has changes that conflict with the next import.
if git show-ref --verify --quiet "refs/remotes/origin/$SYNC_BRANCH"; then
  git checkout --quiet -b "$SYNC_BRANCH" --track "origin/$SYNC_BRANCH"
  git merge --quiet --no-edit "origin/$BASE"
else
  git checkout --quiet -b "$SYNC_BRANCH" "origin/$BASE"
fi

echo "Fetching public Substack RSS from this Mac..."
"$PYTHON" scripts/sync_substack.py

# The imported Markdown files are the *only* files eligible for staging.
# The fresh clone contains no unrelated local changes.
git add -A -- '_posts/*-substack-*.md'
if ! git diff --cached --quiet; then
  git commit --quiet -m "Propose Converses de casa posts from Substack"
fi

if git diff --quiet "origin/$BASE" HEAD -- _posts; then
  echo "No Substack changes to propose."
  exit 0
fi

if [[ "$DRY_RUN" == true ]]; then
  echo "Dry run: would propose these file changes, without pushing or creating a PR:"
  git diff --stat "origin/$BASE" HEAD -- _posts
  exit 0
fi

echo "Pushing review branch $SYNC_BRANCH (never $BASE)..."
git push --quiet --set-upstream origin "$SYNC_BRANCH"
existing_pr="$(gh pr list --repo "$REPO" --head "$SYNC_BRANCH" --base "$BASE" --state open --json url --jq '.[0].url // empty')"

if [[ -n "$existing_pr" ]]; then
  echo "Updated existing review PR: $existing_pr"
else
  gh pr create \
    --repo "$REPO" \
    --base "$BASE" \
    --head "$SYNC_BRANCH" \
    --title "Review: sync Converses de casa posts from Substack (Mac)" \
    --body "Imported from public Substack RSS on the owner's Mac. Posts use the personal category and converses-de-casa tag. Review content, privacy, formatting and language links before merging. This script NEVER publishes or merges automatically."
fi
