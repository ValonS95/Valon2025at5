from user_input_validator import UserInputValidator

# Create two instances
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Sample input lists
inputs1 = ["10", "abc", "-5", "3"]
inputs2 = ["7", "0", "12", "xyz"]

# Validate inputs
valid1 = validator1.validate_positive_integers(inputs1)
valid2 = validator2.validate_positive_integers(inputs2)

# Display validation results
validator1.display_validation_message()
validator2.display_validation_message()