import subprocess
import sys
import json

class LibraryManager:
    def __init__(self, config_path="Config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def install(self, package):
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def check_and_install(self, packages):
        for p in packages:
            try:
                __import__(p)
            except ImportError:
                print(f"{p} missing.")
                if self.config.get("auto_install_libs"):
                    self.install(p)
