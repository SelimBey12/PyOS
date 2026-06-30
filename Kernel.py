import json
import os

class Kernel:
    def __init__(self, config):
        self.config = config
        self.load_files()

    def load_files(self):
        if not os.path.exists("Files.json"):
            with open("Files.json", "w") as f:
                json.dump({}, f)

        with open("Files.json", "r") as f:
            self.files = json.load(f)

    def save_files(self):
        with open("Files.json", "w") as f:
            json.dump(self.files, f, indent=4)

    def run(self, cmd):
        parts = cmd.split()

        if not parts:
            return

        command = parts[0]

        # HELP
        if command == "help":
            print("""
Komutlar:
- help
- echo <text>
- create <file> <content>
- read <file>
- ls
- clear
""")

        # ECHO
        elif command == "echo":
            print(" ".join(parts[1:]))

        # CREATE FILE
        elif command == "create":
            if len(parts) < 3:
                print("Usage: create <file> <content>")
                return
            name = parts[1]
            content = " ".join(parts[2:])
            self.files[name] = content
            self.save_files()
            print(f"{name} created.")

        # READ FILE
        elif command == "read":
            name = parts[1]
            print(self.files.get(name, "File not found."))

        # LIST FILES
        elif command == "ls":
            print("Files:")
            for f in self.files:
                print("-", f)

        # CLEAR
        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        else:
            print("Unknown command:", command)
