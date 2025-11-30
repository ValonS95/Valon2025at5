class UserInputValidator:
    """A class to validate user inputs as positive integers."""

    def __init__(self):
        self.validated = []

    def validate_positive_integers(self, input_list):
        """Returns a list of valid positive integers from the input list of strings."""
        self.validated = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                self.validated.append(int(item))
        return self.validated

    def display_validation_message(self):
        """Displays a message after validation."""
        if self.validated:
            print(f"Validation complete. Valid positive integers: {self.validated}")
        else:
            print("No valid positive integers found.")