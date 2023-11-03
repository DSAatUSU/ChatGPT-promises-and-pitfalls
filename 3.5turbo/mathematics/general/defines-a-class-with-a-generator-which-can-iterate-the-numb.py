class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage
if __name__ == '__main__':
    n = int(input("Enter the range limit: "))
    generator = DivisibleBySevenGenerator(n)
    for num in generator.generate():
        print(num)
