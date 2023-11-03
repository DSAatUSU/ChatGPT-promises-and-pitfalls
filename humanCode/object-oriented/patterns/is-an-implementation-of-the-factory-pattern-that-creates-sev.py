class Dog:
    def bark(self):
        print("Bark!")


class Cat:
    def bark(self):
        print("Meow!")


class Cow:
    def bark(self):
        print("Moo!")


def factory(animal="dog"):
    if (animal == "dog"):
        return Dog()
    elif (animal == "cat"):
        return Cat()
    elif (animal == "cow"):
        return Cow()


dog = factory("dog")
cat = factory("cat")
cow = factory("cow")

dog.bark()
cat.bark()
cow.bark()
