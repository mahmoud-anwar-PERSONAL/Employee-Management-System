from datetime import datetime


class Logger:
    FILE_NAME = "system_log.txt"

    @classmethod
    def log(cls, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {message}\n")
