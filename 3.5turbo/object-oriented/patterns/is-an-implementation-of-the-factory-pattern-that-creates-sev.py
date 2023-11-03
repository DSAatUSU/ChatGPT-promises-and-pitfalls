# Animal base class
class Animal:
    def bark(self):
        pass

# Dog subclass
class Dog(Animal):
    def bark(self):
        print("Woof!")

# Cat subclass
class Cat(Animal):
    def bark(self):
        print("Meow!")

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Main function
def main():
    animal_type = input("Enter animal type (dog/cat): ")
    animal = AnimalFactory.create_animal(animal_type)
    animal.bark()

# Run the main function
if __name__ == "__main__":
    main()
