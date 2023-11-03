class Vehicle:

    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("*The car begins moving*")


class Bicycle(Vehicle):

    def go(self):
        print("*The bicycle begins moving*")


class Boat(Vehicle):
    def go(self):
        print("*The boat begins moving*")


car = Car()
bicycle = Bicycle()
boat = Boat()

racers = [car, bicycle, boat]

for x in racers:
    x.go()
