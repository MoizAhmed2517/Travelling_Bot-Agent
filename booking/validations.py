def get_valid_age(child_number):
    """Prompt the user to enter a valid age between 0 and 17."""
    while True:
        try:
            age = int(input(f"Enter the age of child {child_number}: "))
            if 0 <= age <= 17:
                return f"{age} years old"
            else:
                print("Age must be between 0 and 17. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")