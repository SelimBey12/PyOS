import time
import os

class ErrorLogger:
    def __init__(self, path="errors.psr"):
        self.path = path

    def log(self, error_type, message, module="Kernel"):
        now = time.strftime("%H:%M:%S")
        line = f"[{now}] {error_type} | {message} | {module}\n"

        with open(self.path, "a", encoding="utf-8") as f:
            f.write(line)

        print("⚠ ERROR:", message)
