import random

# Options for the select box
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']

# Generate a random option index
random_option = random.randint(0, len(options) - 1)

# Display the select box
print("Select an option:")
for i, option in enumerate(options):
    print(f"{i+1}. {option}")

# Get user input for the selected option
selected_option = int(input("Enter the number of the option you want to select: "))

# Validate and handle the selected option
if 1 <= selected_option <= len(options):
    print(f"You selected: {options[selected_option - 1]}")
else:
    print("Invalid option selected!")