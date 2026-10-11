from services.employee_manager import EmployeeManager
from services.payroll import Payroll
from services.attendance import Attendance
from utils.input_helpers import (
    get_required_text,
    get_positive_float,
    get_non_negative_int,
)

class EmployeeManagementSystem:
    def __init__(self):
        self.manager = EmployeeManager()
        self.attendance = Attendance(self.manager)
        self.payroll = Payroll()

    def create_employee(self):
        print("\n--- Add Employee ---")
        employee_type = input(
            "Type [1=Full-Time, 2=Part-Time, 3=Freelancer]: "
        ).strip()

        if employee_type not in {"1", "2", "3"}:
            print("Invalid employee type.")
            return

        employee_id = get_required_text("Employee ID: ")
        if self.manager.find_by_id(employee_id):
            print("Employee ID already exists.")
            return

        name = get_required_text("Name: ")
        department = get_required_text("Department: ")
        phone = get_required_text("Phone: ")
        email = get_required_text("Email: ")

        kwargs = {
            "employee_id": employee_id,
            "name": name,
            "department": department,
            "phone": phone,
            "email": email,
        }

        if employee_type == "1":
            kwargs["monthly_salary"] = get_positive_float("Monthly salary: ")
            type_name = "Full-Time"
        elif employee_type == "2":
            kwargs["hourly_rate"] = get_positive_float("Hourly rate: ")
            kwargs["hours_worked"] = get_non_negative_int("Hours worked: ")
            type_name = "Part-Time"
        else:
            kwargs["project_rate"] = get_positive_float("Rate per project: ")
            kwargs["completed_projects"] = get_non_negative_int(
                "Completed projects: "
            )
            type_name = "Freelancer"

        employee = self.manager.build_employee(type_name, kwargs)
        self.manager.add(employee)

    def display_all(self):
        employees = self.manager.get_all()
        if not employees:
            print("No employees found.")
            return

        for employee in employees:
            employee.display()

    def search(self):
        keyword = input("Search by ID, name, or department: ").strip()
        results = self.manager.search(keyword)

        if not results:
            print("No matching employees found.")
            return

        for employee in results:
            employee.display()

    def update(self):
        employee_id = get_required_text("Employee ID: ")
        employee = self.manager.find_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return

        print("Press Enter to keep the current value.")
        name = input(f"Name [{employee.name}]: ").strip()
        department = input(f"Department [{employee.department}]: ").strip()
        phone = input(f"Phone [{employee.phone}]: ").strip()
        email = input(f"Email [{employee.email}]: ").strip()

        if name:
            employee.name = name
        if department:
            employee.department = department
        if phone:
            employee.phone = phone
        if email:
            employee.email = email

        self.manager.update_type_specific_data(employee)
        self.manager.save()
        print("Employee updated successfully.")

    def delete(self):
        employee_id = get_required_text("Employee ID: ")
        self.manager.delete(employee_id)

    def attendance_menu(self):
        employee_id = get_required_text("Employee ID: ")
        print("1. Present")
        print("2. Absent")
        print("3. Late")
        choice = input("Choose: ").strip()

        statuses = {"1": "present", "2": "absent", "3": "late"}
        if choice not in statuses:
            print("Invalid choice.")
            return

        self.attendance.record(employee_id, statuses[choice])

    def bonus_deduction_menu(self):
        employee_id = get_required_text("Employee ID: ")
        employee = self.manager.find_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return

        print("1. Add bonus")
        print("2. Add deduction")
        choice = input("Choose: ").strip()
        amount = get_positive_float("Amount: ")

        try:
            if choice == "1":
                employee.add_bonus(amount)
                action = "Bonus"
            elif choice == "2":
                employee.add_deduction(amount)
                action = "Deduction"
            else:
                print("Invalid choice.")
                return

            self.manager.save()
            print(f"{action} added successfully.")
        except ValueError as exc:
            print(exc)

    def salary(self):
        employee_id = get_required_text("Employee ID: ")
        employee = self.manager.find_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return

        self.payroll.display_employee_salary(employee)

    def report(self):
        self.payroll.generate_report(self.manager.get_all())

    def statistics(self):
        stats = self.manager.statistics()

        print("\n--- Statistics ---")
        print(f"Total employees: {stats['total_employees']}")
        print(f"Total payroll: {stats['total_payroll']:.2f}")
        print("\nEmployees by department:")

        for department, count in stats["departments"].items():
            print(f"- {department}: {count}")

    def run(self):
        while True:
            print("\n" + "=" * 50)
            print("       EMPLOYEE MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1. Add employee")
            print("2. Display all employees")
            print("3. Search employee")
            print("4. Update employee")
            print("5. Delete employee")
            print("6. Record attendance")
            print("7. Add bonus/deduction")
            print("8. Calculate salary")
            print("9. Generate payroll report")
            print("10. Statistics")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            try:
                actions = {
                    "1": self.create_employee,
                    "2": self.display_all,
                    "3": self.search,
                    "4": self.update,
                    "5": self.delete,
                    "6": self.attendance_menu,
                    "7": self.bonus_deduction_menu,
                    "8": self.salary,
                    "9": self.report,
                    "10": self.statistics,
                }

                if choice == "0":
                    print("Goodbye!")
                    break

                action = actions.get(choice)
                if action:
                    action()
                else:
                    print("Invalid option.")

            except (ValueError, OSError) as exc:
                print(f"Operation failed: {exc}")


if __name__ == "__main__":
    EmployeeManagementSystem().run()
