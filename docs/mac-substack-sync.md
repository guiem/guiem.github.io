# Run Converses de casa Substack sync from a Mac

This replaces the unreliable **cloud-hosted RSS download** with a local macOS job.
It still uses the existing `scripts/sync_substack.py` converter and creates or updates
a **review-only GitHub pull request**. It never commits to `master`, merges, or publishes.

## Requirements

- A Mac with Internet access and permission to access `https://gboschbo.substack.com/feed`
  using the **Terminal** `curl` command. A feed working in Safari/Chrome does not
  guarantee `curl` succeeds, so test it below.
- Git, Python **3.10+**, `curl`, and [GitHub CLI](https://cli.github.com/).
  With Homebrew, install missing tools using `brew install git python gh`.
- GitHub CLI logged in as an account that can push a new branch and open a PR
  in `guiem/guiem.github.io`.
- A clone of this repository containing this setup PR **after it is merged**.

## One-time installation

In Terminal:

```bash
git clone git@github.com:guiem/guiem.github.io.git
cd guiem.github.io
gh auth login
gh auth setup-git

# Check Substack from the Mac itself:
curl -sSL -o /dev/null -w 'Substack HTTP %{http_code}\n' https://gboschbo.substack.com/feed

# Install Python libraries and a per-user daily launchd job:
bash scripts/install_substack_mac_sync.sh
```

If you already have a local clone, use it instead of cloning again.
If you prefer HTTPS, clone using `gh repo clone guiem/guiem.github.io`.
The scripts use `gh` authentication for branch pushes and PR creation.

**Before first real sync**, inspect the planned changes:

```bash
bash scripts/run_substack_mac_sync.sh --dry-run
```

If the dry run looks correct, submit a review PR:

```bash
bash scripts/run_substack_mac_sync.sh
```

## What happens daily

The installer writes a *user* LaunchAgent named
`~/Library/LaunchAgents/com.guiem.converses-substack-sync.plist`, scheduled
for **09:00 local Mac time**. It runs only while your Mac and user session are
available; missed scheduled jobs may be invoked when the Mac wakes.

Each run:

1. Clones the current GitHub repository to a disposable temporary directory;
   it does **not** alter your working tree.
2. Reuses `automation/substack-converses-mac` if it exists, or creates it
   from `master`. It merges current `master` before importing; conflicting
   updates fail safely rather than force-pushing.
3. Fetches public Substack RSS **from your Mac** and validates the feed.
4. Generates Jekyll Markdown files under `_posts/` with category `personal`
   and tag `converses-de-casa` using the existing importer.
5. Pushes only the dedicated review branch and opens or updates an **open PR**
   targeting `master`, *if there are changes*. It never merges anything.

The existing GitHub-hosted `Propose Substack conversation sync` workflow
should **remain disabled** to avoid the blocked cloud requests and duplicate
review PRs. The local script does not require a self-hosted runner.

## Logs and controls

```bash
# View the local run log
tail -n 80 ~/Library/Logs/converses-substack-sync.log

# Trigger the scheduled job immediately, if installed
launchctl kickstart "gui/$(id -u)/com.guiem.converses-substack-sync"

# Disable the schedule (does not delete any PR)
launchctl bootout "gui/$(id -u)" ~/Library/LaunchAgents/com.guiem.converses-substack-sync.plist

# Re-enable the schedule
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.guiem.converses-substack-sync.plist
```

To **uninstall**, run `launchctl bootout` as above and remove the plist.
Your GitHub repository is unaffected.

## Limitations and security

- Run the `curl` check before installing: the Mac's outgoing IP may work where
  GitHub Actions fails, but this is not guaranteed.
- `gh auth login` creates credentials on the Mac. Do not copy tokens into
  scripts or commits.
- The GitHub repo and review PRs are public; imported content is visible in a
  PR even before you merge it.
- RSS exposes recent published articles, not a complete historical Substack
  archive. Images are linked remotely.
- Translation groups are still managed by `_data/substack_translations.json`.
  Check the language switcher and privacy of every proposed import.
- If the Mac is shut down or unavailable, the sync cannot run at that moment.
