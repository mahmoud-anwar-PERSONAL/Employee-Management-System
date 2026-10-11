import json
import os


class FileManager:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_NAME = os.path.join(BASE_DIR, "data", "employees.json")

    @classmethod
    def load(cls):
        if not os.path.exists(cls.FILE_NAME):
            return []

        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    @classmethod
    def save(cls, employees):
        os.makedirs(os.path.dirname(cls.FILE_NAME), exist_ok=True)

        with open(cls.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                [employee.to_dict() for employee in employees],
                file,
                ensure_ascii=False,
                indent=4,
            )