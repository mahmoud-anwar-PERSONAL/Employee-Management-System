from abc import ABC, abstractmethod


class Employee(ABC):
    ABSENCE_DEDUCTION = 200.0
    LATE_DEDUCTION = 50.0

    def __init__(
        self,
        employee_id,
        name,
        department,
        phone,
        email,
        bonus=0,
        extra_deduction=0,
        present_days=0,
        absent_days=0,
        late_days=0,
    ):
        self.employee_id = str(employee_id)
        self.name = name
        self.department = department
        self.phone = phone
        self.email = email
        self.bonus = float(bonus)
        self.extra_deduction = float(extra_deduction)
        self.present_days = int(present_days)
        self.absent_days = int(absent_days)
        self.late_days = int(late_days)

    @property
    @abstractmethod
    def employee_type(self):
        pass

    @abstractmethod
    def calculate_base_salary(self):
        pass

    @abstractmethod
    def type_specific_data(self):
        pass

    def calculate_deductions(self):
        return (
            self.absent_days * self.ABSENCE_DEDUCTION
            + self.late_days * self.LATE_DEDUCTION
            + self.extra_deduction
        )

    def calculate_final_salary(self):
        return max(
            0.0,
            self.calculate_base_salary()
            + self.bonus
            - self.calculate_deductions(),
        )

    def mark_attendance(self, status):
        status = status.lower()
        if status == "present":
            self.present_days += 1
        elif status == "absent":
            self.absent_days += 1
        elif status == "late":
            self.late_days += 1
        else:
            raise ValueError("Invalid attendance status.")

    def add_bonus(self, amount):
        if amount <= 0:
            raise ValueError("Bonus must be greater than zero.")
        self.bonus += amount

    def add_deduction(self, amount):
        if amount <= 0:
            raise ValueError("Deduction must be greater than zero.")
        self.extra_deduction += amount

    def to_dict(self):
        return {
            "id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "phone": self.phone,
            "email": self.email,
            "employee_type": self.employee_type,
            "bonus": self.bonus,
            "extra_deduction": self.extra_deduction,
            "present_days": self.present_days,
            "absent_days": self.absent_days,
            "late_days": self.late_days,
            **self.type_specific_data(),
        }

    def display(self):
        print("\n" + "-" * 50)
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Type: {self.employee_type}")
        print(f"Base Salary: {self.calculate_base_salary():.2f}")
        print(f"Bonus: {self.bonus:.2f}")
        print(f"Deductions: {self.calculate_deductions():.2f}")
        print(f"Final Salary: {self.calculate_final_salary():.2f}")
        print(
            f"Attendance: Present={self.present_days}, "
            f"Absent={self.absent_days}, Late={self.late_days}"
        )
        print("-" * 50)
