# 🛠️ Klipper: Configurable TRSYNC_TIMEOUT with Automated Workflow

This repo makes Klipper’s `TRSYNC_TIMEOUT` value configurable through an external `.cfg` file—and ensures the patch re-applies automatically after every Klipper update. Ideal for advanced setups with multiple MCUs or sync-sensitive hardware.

## 🚀 What This Includes

- 🔧 Patch to `klippy/mcu.py` using Python's `configparser`
- 🗂 External config file: `trsync.cfg`, avoids breaking Klipper's native validation
- 🤖 Patch automation: a Python script + bash update flow
- ✅ Sanity check tool to confirm runtime values
- 🔁 Optional Moonraker/Mainsail integration via post-update hook

## 📦 Included Files

| File                      | Purpose                                         |
|---------------------------|-------------------------------------------------|
| `update_trsync_timeout.py`| Applies the patch to `mcu.py`                   |
| `check_trsync_timeout.py` | Prints the current timeout from your config     |
| `update-klipper.sh`       | Automates updates + patch reapplication         |
| `trsync_timeout.patch`    | Unified diff backup patch (optional)            |
| `trsync.cfg`              | External config file (not validated by Klipper) |

## 📜 License

MIT for code. Documentation may be covered by [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

# 📥 Klipper TRSYNC_TIMEOUT Installation Script

# 🔧 Step 1: Patch Klipper's mcu.py
```bash
python3 ~/update_trsync_timeout.py
```

# 🗂 Step 2: Create the external config file
```bash
cat << EOF > /home/biqu/printer_data/config/trsync.cfg
[mcu]
trsync_timeout = 0.05
EOF
```

# 🔁 Step 3: Automate Klipper updates
```bash
chmod +x ~/klipper/update-klipper.sh
~/klipper/update-klipper.sh
```

# Optional: Add a shell alias for future updates
```bash
echo "alias klipper-update='~/klipper/update-klipper.sh'" >> ~/.bashrc
source ~/.bashrc
```

# 🧪 Step 4: Validate that your config is being read correctly
```bash
python3 ~/check_trsync_timeout.py
```

# 🧩 Step 5: (Optional) Auto-patch after Moonraker/Mainsail updates

# Add post-update hook to Moonraker config
```bash
echo -e '[update_manager klipper]\npost_update: ~/klipper/.update-trsync-timeout.sh' >> ~/klipper/moonraker.conf
```
# Create the hook script
```bash
cat << 'EOS' > ~/klipper/.update-trsync-timeout.sh
#!/bin/bash
python3 /home/biqu/update_trsync_timeout.py
sudo systemctl restart klipper
EOS
```

# Make the hook executable
```bash
chmod +x ~/klipper/.update-trsync-timeout.sh
```

# ✅ Done! Your TRSYNC_TIMEOUT is now configurable and persistent.


