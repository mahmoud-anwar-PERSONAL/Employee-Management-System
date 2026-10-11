from models import (
    FullTimeEmployee,
    PartTimeEmployee,
    Freelancer,
)
from utils.file_manager import FileManager
from utils.logger import Logger
from utils.input_helpers import get_non_negative_int, get_positive_float


class EmployeeManager:
    TYPE_MAP = {
        "Full-Time": FullTimeEmployee,
        "Part-Time": PartTimeEmployee,
        "Freelancer": Freelancer,
    }

    def __init__(self):
        self.employees = []
        self.load()

    def build_employee(self, employee_type, data):
        employee_class = self.TYPE_MAP[employee_type]
        return employee_class(**data)

    def load(self):
        self.employees = []

        for data in FileManager.load():
            try:
                employee_type = data.pop("employee_type")
                employee = self.build_employee(employee_type, {
                    "employee_id": data.pop("id"),
                    **data,
                })
                self.employees.append(employee)
            except (KeyError, TypeError, ValueError):
                Logger.log("Skipped invalid employee record.")

    def save(self):
        FileManager.save(self.employees)

    def get_all(self):
        return list(self.employees)

    def find_by_id(self, employee_id):
        employee_id = str(employee_id)
        return next(
            (
                employee
                for employee in self.employees
                if employee.employee_id == employee_id
            ),
            None,
        )

    def add(self, employee):
        if self.find_by_id(employee.employee_id):
            raise ValueError("Employee ID already exists.")

        self.employees.append(employee)
        self.save()
        Logger.log(f"Employee {employee.employee_id} added.")
        print("Employee added successfully.")

    def delete(self, employee_id):
        employee = self.find_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return

        self.employees.remove(employee)
        self.save()
        Logger.log(f"Employee {employee_id} deleted.")
        print("Employee deleted successfully.")

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            employee
            for employee in self.employees
            if keyword in employee.employee_id.lower()
            or keyword in employee.name.lower()
            or keyword in employee.department.lower()
        ]

    def update_type_specific_data(self, employee):
        if isinstance(employee, FullTimeEmployee):
            value = input(
                f"Monthly salary [{employee.monthly_salary}]: "
            ).strip()
            if value:
                employee.monthly_salary = get_positive_float(
                    f"Confirm monthly salary [{value}]: "
                )

        elif isinstance(employee, PartTimeEmployee):
            value = input(
                f"Hourly rate [{employee.hourly_rate}]: "
            ).strip()
            if value:
                employee.hourly_rate = get_positive_float(
                    f"Confirm hourly rate [{value}]: "
                )

            value = input(
                f"Hours worked [{employee.hours_worked}]: "
            ).strip()
            if value:
                employee.hours_worked = get_non_negative_int(
                    f"Confirm hours worked [{value}]: "
                )

        elif isinstance(employee, Freelancer):
            value = input(
                f"Project rate [{employee.project_rate}]: "
            ).strip()
            if value:
                employee.project_rate = get_positive_float(
                    f"Confirm project rate [{value}]: "
                )

            value = input(
                f"Completed projects [{employee.completed_projects}]: "
            ).strip()
            if value:
                employee.completed_projects = get_non_negative_int(
                    f"Confirm completed projects [{value}]: "
                )

        Logger.log(f"Employee {employee.employee_id} updated.")

    def statistics(self):
        departments = {}

        for employee in self.employees:
            departments[employee.department] = (
                departments.get(employee.department, 0) + 1
            )

        total_payroll = sum(
            employee.calculate_final_salary()
            for employee in self.employees
        )

        return {
            "total_employees": len(self.employees),
            "total_payroll": total_payroll,
            "departments": departments,
        }
