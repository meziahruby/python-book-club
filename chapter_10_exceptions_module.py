def addition(a, b):
    """Adds two numbers if they are both numbers"""

    try:
        result = int(a) + int(b)
    except ValueError:
        # Using ValueError instead of TypeError to catch error when trying to convert text to int
        print("Sorry, at least one input is not a number. Please try again.\n")
    else:
        print(f"The sum is {result}.\n")

