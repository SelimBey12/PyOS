import json
import os

print("PyOS Setup starting...")

config = {
    "os_name": "PyOS",
    "version": "0.1",
    "user": "admin"
}

with open("Config.json", "w") as f:
    json.dump(config, f, indent=4)

if not os.path.exists("Files.json"):
    with open("Files.json", "w") as f:
        json.dump({}, f)

print("Setup complete.")
