import json
import os

class Kernel:
    def __init__(self, config, err):
        self.config = config
        self.err = err
        self.load_files()

    # ---------------- FILE SYSTEM ----------------
    def load_files(self):
        try:
            if not os.path.exists("Files.json"):
                with open("Files.json", "w", encoding="utf-8") as f:
                    json.dump({}, f)

            with open("Files.json", "r", encoding="utf-8") as f:
                self.files = json.load(f)

        except Exception as e:
            self.err.log("FILE_SYSTEM_ERROR", str(e), "Kernel")
            self.files = {}

    def save_files(self):
        try:
            with open("Files.json", "w", encoding="utf-8") as f:
                json.dump(self.files, f, indent=4)
        except Exception as e:
            self.err.log("FILE_SAVE_ERROR", str(e), "Kernel")

    # ---------------- COMMAND HANDLER ----------------
    def run(self, cmd):
        try:
            parts = cmd.strip().split()
            if not parts:
                return

            command = parts[0].lower()

            # ---------------- HELP ----------------
            if command == "help":
                print("""
📌 PyOS Komutları:
- help              -> komut listesi
- echo <text>       -> yazı yazdır
- create <f> <txt>  -> dosya oluştur
- read <f>          -> dosya oku
- del <f>           -> dosya sil
- ls                -> dosyaları listele
- clear             -> ekran temizle
""")

            # ---------------- ECHO ----------------
            elif command == "echo":
                print(" ".join(parts[1:]))

            # ---------------- CREATE FILE ----------------
            elif command == "create":
                if len(parts) < 3:
                    print("Usage: create <file> <content>")
                    return

                name = parts[1]
                content = " ".join(parts[2:])

                self.files[name] = content
                self.save_files()

                print(f"[OK] {name} created.")

            # ---------------- READ FILE ----------------
            elif command == "read":
                if len(parts) < 2:
                    print("Usage: read <file>")
                    return

                name = parts[1]
                print(self.files.get(name, "[ERROR] File not found."))

            # ---------------- DELETE FILE ----------------
            elif command == "del":
                if len(parts) < 2:
                    print("Usage: del <file>")
                    return

                name = parts[1]

                if name in self.files:
                    del self.files[name]
                    self.save_files()
                    print(f"[OK] {name} deleted.")
                else:
                    print("[ERROR] File not found.")

            # ---------------- LIST FILES ----------------
            elif command == "ls":
                if not self.files:
                    print("No files.")
                    return

                print("📁 Files:")
                for f in self.files:
                    print(" -", f)

            # ---------------- CLEAR SCREEN ----------------
            elif command == "clear":
                os.system("cls" if os.name == "nt" else "clear")

            # ---------------- UNKNOWN COMMAND ----------------
            else:
                print(f"[ERROR] Unknown command: {command}")

        except Exception as e:
            self.err.log("KERNEL_RUNTIME_ERROR", str(e), "Kernel.run")
            print("Kernel crashed a bit check .psr log")
