import json
import sys

from Kernel import Kernel
from libraries import LibraryManager
from Error import ErrorLogger

print("PyOS Booting...")

# ---------------- CONFIG LOAD ----------------
try:
    with open("Config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except Exception as e:
    print("Config load failed, using fallback config.")
    config = {
        "os_name": "PyOS",
        "version": "0.1",
        "user": "admin",
        "auto_install_libs": True,
        "debug_mode": True
    }

# ---------------- ERROR SYSTEM ----------------
err = ErrorLogger()

# ---------------- LIBRARY SYSTEM ----------------
libs = LibraryManager()

required_libs = [
    "json",
    "os",
    "time"
]

try:
    if config.get("auto_install_libs", True):
        libs.check_and_install(required_libs)
except Exception as e:
    err.log("LIBRARY_BOOT_FAIL", str(e), "OS.py")

# ---------------- KERNEL START ----------------
kernel = Kernel(config, err)

print("\nPyOS Ready.")
print("Type 'help' for commands.")
print("Type 'shutdown' to exit.\n")

# ---------------- MAIN LOOP ----------------
while True:
    try:
        cmd = input("PyOS> ")

        if cmd.lower() in ["exit", "shutdown"]:
            print("Shutting down PyOS...")
            break

        kernel.run(cmd)

    except Exception as e:
        err.log("RUNTIME_ERROR", str(e), "OS_LOOP")
        print("Something went wrong, check .psr log.")
