class Payroll:
    REPORT_FILE = "reports/payroll_report.txt"

    @staticmethod
    def display_employee_salary(employee):
        print("\n--- Salary Details ---")
        print(f"Employee: {employee.name}")
        print(f"Type: {employee.employee_type}")
        print(f"Base Salary: {employee.calculate_base_salary():.2f}")
        print(f"Bonus: {employee.bonus:.2f}")
        print(f"Deductions: {employee.calculate_deductions():.2f}")
        print(f"Final Salary: {employee.calculate_final_salary():.2f}")

    @classmethod
    def generate_report(cls, employees):
        total = 0.0

        with open(cls.REPORT_FILE, "w", encoding="utf-8") as file:
            file.write("EMPLOYEE PAYROLL REPORT\n")
            file.write("=" * 70 + "\n")

            for employee in employees:
                salary = employee.calculate_final_salary()
                total += salary
                file.write(
                    f"ID: {employee.employee_id} | "
                    f"Name: {employee.name} | "
                    f"Type: {employee.employee_type} | "
                    f"Salary: {salary:.2f}\n"
                )

            file.write("=" * 70 + "\n")
            file.write(f"Total Payroll: {total:.2f}\n")

        print(f"Payroll report generated: {cls.REPORT_FILE}")
