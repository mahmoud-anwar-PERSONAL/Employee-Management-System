def get_required_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field is required.")


def get_positive_float(message):
    while True:
        try:
            value = float(input(message).strip())
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_non_negative_int(message):
    while True:
        try:
            value = int(input(message).strip())
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")
