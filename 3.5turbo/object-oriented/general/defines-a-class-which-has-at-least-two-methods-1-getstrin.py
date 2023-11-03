class MyString:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

def test():
    my_string = MyString()
    my_string.getString()
    my_string.printString()

if __name__ == "__main__":
    test()
