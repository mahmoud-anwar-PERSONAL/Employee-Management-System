from .employee import Employee


class FullTimeEmployee(Employee):
    def __init__(self, *args, monthly_salary=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.monthly_salary = float(monthly_salary)

    @property
    def employee_type(self):
        return "Full-Time"

    def calculate_base_salary(self):
        return self.monthly_salary

    def type_specific_data(self):
        return {"monthly_salary": self.monthly_salary}
