# Contains utility functions.

def validate_input(input_value, valid_options):
    if input_value in valid_options:
        return True
    print(f"Invalid input: {input_value}. Valid options are: {valid_options}")
    return False

