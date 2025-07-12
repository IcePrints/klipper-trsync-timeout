# klipper-trsync-timeout
Make Klipper’s TRSYNC_TIMEOUT configurable via an external .cfg file, with automated patching and update-safe validation. Ideal for multi-MCU setups where homing reliability and timing precision matter.

# 🛠️ Klipper: Configurable TRSYNC_TIMEOUT with Automated Workflow

This repo makes Klipper’s `TRSYNC_TIMEOUT` value configurable through an external `.cfg` file—and ensures the patch re-applies automatically after every Klipper update. Ideal for advanced setups with multiple MCUs or sync-sensitive hardware.

## 🚀 What This Includes

- 🔧 Patch to `klippy/mcu.py` using Python's `configparser`
- 🗂 External config file: `trsync.cfg`, avoids breaking Klipper's native validation
- 🤖 Patch automation: a Python script + bash update flow
- ✅ Sanity check tool to confirm your active timeout value
- 🔁 Optional Moonraker/Mainsail integration via post-update hook

---

## 🧩 External Config Setup

Create this file at `/home/biqu/printer_data/config/trsync.cfg`:

```ini
[mcu]
trsync_timeout = 0.05
