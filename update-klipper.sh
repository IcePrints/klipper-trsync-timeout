#!/bin/bash
echo "🔄 Updating Klipper..."
cd ~/klipper || exit
git pull

echo "🔧 Reapplying TRSYNC_TIMEOUT patch..."
python3 ~/update_trsync_timeout.py

echo "🧪 Checking timeout value..."
python3 ~/check_trsync_timeout.py

echo "🚀 Restarting Klipper..."
sudo systemctl restart klipper
echo "✅ Done."
