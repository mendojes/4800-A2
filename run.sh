#!/usr/bin/env bash
set -euo pipefail

# CONFIG - update to your app's path
APP_DIR="$HOME/4800-A2"    # change if needed
APP_CMD="python3.13 app.py"
LOG_FILE="$APP_DIR/log.txt"
GIT_BRANCH="main"

echo "===== Deploy started at $(date -u) =====" >> "$LOG_FILE"

cd "$APP_DIR" || { echo "ERROR: app dir not found: $APP_DIR" >> "$LOG_FILE"; exit 1; }

# make sure we're on the right branch
git fetch origin
git checkout "$GIT_BRANCH"
git pull --rebase

# optional: install/upgrade dependencies
if [ -f "$APP_DIR/requirements.txt" ]; then
  python3.13 -m pip install --upgrade -r requirements.txt >> "$LOG_FILE" 2>&1 || echo "pip install returned non-zero" >> "$LOG_FILE"
fi

# kill existing process(es) for this app (simple approach)
# adjust grep pattern to match your app if necessary
PIDS=$(pgrep -f "python3.13 .*app.py" || true)
if [ -n "$PIDS" ]; then
  echo "Killing existing process(es): $PIDS" >> "$LOG_FILE"
  kill $PIDS || true
  sleep 2
fi

# start the app in background using nohup
nohup $APP_CMD > "$LOG_FILE" 2>&1 &

echo "Deploy finished at $(date -u). App started with PID(s): $(pgrep -f "python3.13 .*app.py" || true)" >> "$LOG_FILE"