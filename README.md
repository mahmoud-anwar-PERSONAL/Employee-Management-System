# Employee Management System

A console-based Employee Management System built with **Python and Object-Oriented Programming (OOP)**.

This project is designed as a portfolio-quality example demonstrating clean project structure, inheritance, abstraction, polymorphism, JSON persistence, payroll calculations, attendance tracking, logging, and report generation.

## Features

- Add, update, search, and delete employees
- Support for:
  - Full-Time employees
  - Part-Time employees
  - Freelancers
- Attendance tracking:
  - Present
  - Absent
  - Late
- Automatic salary calculations
- Bonuses and additional deductions
- Payroll report generation
- Department statistics
- JSON-based data persistence
- Activity logging
- Input validation
- Modular OOP architecture

## OOP Concepts Demonstrated

### Encapsulation
Employee data and behavior are grouped inside dedicated classes.

### Inheritance
`FullTimeEmployee`, `PartTimeEmployee`, and `Freelancer` inherit from the abstract `Employee` class.

### Abstraction
The `Employee` class defines common behavior while requiring subclasses to implement salary-related methods.

### Polymorphism
`calculate_base_salary()` behaves differently for each employee type while the payroll system uses the same interface.

## Project Structure

```text
Employee_Management_System/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── employee.py
│   ├── full_time_employee.py
│   ├── part_time_employee.py
│   ├── freelancer.py
│   └── __init__.py
│
├── services/
│   ├── employee_manager.py
│   ├── attendance.py
│   ├── payroll.py
│   └── __init__.py
│
├── utils/
│   ├── file_manager.py
│   ├── input_helpers.py
│   ├── logger.py
│   └── __init__.py
│
├── data/
│   └── employees.json
│
└── reports/
    └── payroll_report.txt
```

## Requirements

- Python 3.10 or newer
- No external libraries are required.

## How to Run

1. Clone or download the project.
2. Open a terminal inside the project folder.
3. Run:

```bash
python main.py
```

## Sample Employee Types

### Full-Time
Salary is based on a fixed monthly salary.

### Part-Time
Salary is calculated using:

```text
hourly rate × hours worked
```

### Freelancer
Salary is calculated using:

```text
project rate × completed projects
```

## Salary Rules

The demo project uses:

- Absence deduction: 200 per day
- Late deduction: 50 per day
- Additional employee deductions
- Employee bonuses

Final salary cannot become negative.

## Data and Reports

Employee data is stored in:

```text
data/employees.json
```

System actions are logged in:

```text
system_log.txt
```

Payroll reports are generated in:

```text
reports/payroll_report.txt
```

## Portfolio Notes

This project is intended as a demonstration of Python OOP and software organization. For production use, the persistence layer could be upgraded from JSON to SQLite/PostgreSQL and the console interface could be replaced with a GUI or web interface.

## Author

Python OOP Portfolio Project
