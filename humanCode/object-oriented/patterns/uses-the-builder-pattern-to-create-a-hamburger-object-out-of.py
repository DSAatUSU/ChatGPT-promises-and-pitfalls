class Cheese:
    def whatisit(self):
        print("Cheese")

class Bun:
    def whatisit(self):
        print("Bun")

class Lettuce:
    def whatisit(self):
        print("Lettuce")

class BeefPatty:
    def whatisit(self):
        print("BeefPatty")

class ChickenPatty:
    def whatisit(self):
        print("ChickenPatty")

class Tomato:
    def whatisit(self):
        print("Tomato")

class Hamburger:
    composition = []
    def add(self, type):
        if type == "cheese":
            self.composition.append(Cheese())
        elif type == "bun":
            self.composition.append(Bun())
        elif type == "lettuce":
            self.composition.append(Lettuce())
        elif type == "beef-patty":
            self.composition.append(BeefPatty())
        elif type == "chicken-patty":
            self.composition.append(ChickenPatty())
        elif type == "tomato":
            self.composition.append(Tomato())

    def whatIsInIt(self):
        for ing in self.composition:
            ing.whatisit()

class HamburgerBuilder:
    burger = Hamburger()
    def Hamburger(self):
        return self.burger

    def reset(self):
        self.burger = Hamburger()

    def addCheese(self):
        self.burger.add("cheese")

    def addBun(self):
        self.burger.add("bun")

    def addLettuce(self):
        self.burger.add("lettuce")

    def addBeefPatty(self):
        self.burger.add("beef-patty")

    def addChickenPatty(self):
        self.burger.add("chicken-patty")

    def addTomato(self):
        self.burger.add("tomato")

if __name__ == "__main__":
    builder = HamburgerBuilder()
    builder.addBun()
    builder.addLettuce()
    builder.addTomato()
    builder.addCheese()
    builder.addBeefPatty()
    builder.addCheese()
    builder.addBeefPatty()
    builder.addBun()

    burger = builder.Hamburger()

    burger.whatIsInIt()


