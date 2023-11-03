class Animal:
    def go(self):
        print("The Animal is going!")


class Dog(Animal):
    def go(self):
        print("The Dog is going!")


class Cat(Animal):
    def go(self):
        print("The Cat is going!")


def main():
    # Create instances of each class
    animal = Animal()
    dog = Dog()
    cat = Cat()

    # Call the go() method on each instance
    animal.go()  # The Animal is going!
    dog.go()  # The Dog is going!
    cat.go()  # The Cat is going!


if __name__ == '__main__':
    main()
