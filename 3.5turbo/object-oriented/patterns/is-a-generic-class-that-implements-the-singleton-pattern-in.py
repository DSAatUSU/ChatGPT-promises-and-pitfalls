class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Check if an instance of the class already exists
        if cls not in cls._instances:
            # If not, create a new instance and store it in the class dictionary
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingletonClass(metaclass=Singleton):
    def __init__(self, data):
        self.data = data

# Usage example
if __name__ == "__main__":
    # Create two instances of MySingletonClass
    singleton1 = MySingletonClass("Hello")
    singleton2 = MySingletonClass("World")

    # Both instances should have the same data
    print(singleton1.data)  # Output: Hello
    print(singleton2.data)  # Output: Hello
    print(singleton1 is singleton2)  # Output: True
