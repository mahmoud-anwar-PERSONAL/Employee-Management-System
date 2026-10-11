from .employee import Employee


class Freelancer(Employee):
    def __init__(
        self,
        *args,
        project_rate=0,
        completed_projects=0,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.project_rate = float(project_rate)
        self.completed_projects = int(completed_projects)

    @property
    def employee_type(self):
        return "Freelancer"

    def calculate_base_salary(self):
        return self.project_rate * self.completed_projects

    def type_specific_data(self):
        return {
            "project_rate": self.project_rate,
            "completed_projects": self.completed_projects,
        }
