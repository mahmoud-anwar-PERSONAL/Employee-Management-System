from .employee import Employee


class PartTimeEmployee(Employee):
    def __init__(self, *args, hourly_rate=0, hours_worked=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)

    @property
    def employee_type(self):
        return "Part-Time"

    def calculate_base_salary(self):
        return self.hourly_rate * self.hours_worked

    def type_specific_data(self):
        return {
            "hourly_rate": self.hourly_rate,
            "hours_worked": self.hours_worked,
        }
