from utils.logger import Logger


class Attendance:
    def __init__(self, employee_manager):
        self.employee_manager = employee_manager

    def record(self, employee_id, status):
        employee = self.employee_manager.find_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return

        employee.mark_attendance(status)
        self.employee_manager.save()

        Logger.log(
            f"Attendance recorded: employee={employee_id}, status={status}"
        )
        print("Attendance recorded successfully.")
