#!/usr/bin/env bash
# Installs a per-user launchd job. Run this once, on your own Mac, after merging.
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.guiem.converses-substack-sync"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
RUNNER="$ROOT/scripts/run_substack_mac_sync.sh"
LOG="$HOME/Library/Logs/converses-substack-sync.log"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This installer must run on macOS." >&2
  exit 1
fi
for binary in python3 git gh curl launchctl; do
  command -v "$binary" >/dev/null || { echo "Missing prerequisite: $binary" >&2; exit 1; }
done
python3 -c 'import sys; assert sys.version_info >= (3, 10), "Python 3.10+ is required"'
gh auth status >/dev/null 2>&1 || {
  echo "Run 'gh auth login' and 'gh auth setup-git' first." >&2
  exit 1
}

echo "Preparing Python dependencies..."
python3 -m venv "$ROOT/.venv-substack"
"$ROOT/.venv-substack/bin/python" -m pip install \
  'feedparser>=6,<7' 'beautifulsoup4>=4,<5' 'markdownify>=1,<2'

mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
"$ROOT/.venv-substack/bin/python" - "$LABEL" "$RUNNER" "$PLIST" "$LOG" <<'PY'
import plistlib
import sys
from pathlib import Path

label, runner, plist, log = sys.argv[1:]
data = {
    "Label": label,
    "ProgramArguments": ["/bin/bash", runner],
    "StartCalendarInterval": {"Hour": 9, "Minute": 0},
    "RunAtLoad": False,
    "StandardOutPath": log,
    "StandardErrorPath": log,
}
Path(plist).write_bytes(plistlib.dumps(data))
PY

launchctl bootout "gui/$(id -u)" "$PLIST" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo ""
echo "Installed: $PLIST"
echo "Daily schedule: 09:00 local Mac time (while logged in; macOS may run after wake)."
echo "To run immediately: bash '$RUNNER'"
echo "To read logs: tail -n 80 '$LOG'"
echo "To uninstall: launchctl bootout gui/$(id -u) '$PLIST'; rm '$PLIST'"
echo "The sync creates/updates review PRs only. Nothing is merged."
