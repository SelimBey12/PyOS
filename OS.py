import json
from Kernel import Kernel

print("PyOS Booting...")

with open("Config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

kernel = Kernel(config)

print("PyOS Ready.\nType 'help' for commands.\n")

while True:
    cmd = input("PyOS> ")
    
    if cmd.lower() in ["exit", "shutdown"]:
        print("Shutting down PyOS...")
        break

    kernel.run(cmd)
