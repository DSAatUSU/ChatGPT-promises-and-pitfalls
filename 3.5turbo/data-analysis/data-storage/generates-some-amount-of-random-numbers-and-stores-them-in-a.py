import random

def generate_random_numbers(num_of_numbers):
    """Generates random numbers and stores them in a file"""
    random_numbers = []
    for _ in range(num_of_numbers):
        random_numbers.append(random.randint(1, 100))
    
    with open("random_numbers.txt", "w") as file:
        for number in random_numbers:
            file.write(str(number) + "\n")
    print(f"{num_of_numbers} random numbers generated and saved in random_numbers.txt")

# Prompt the user to enter the number of random numbers to generate
num_of_numbers = int(input("Enter the number of random numbers to generate: "))

generate_random_numbers(num_of_numbers)
