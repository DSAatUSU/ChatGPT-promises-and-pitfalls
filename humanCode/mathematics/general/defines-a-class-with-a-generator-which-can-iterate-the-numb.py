class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            yield i * 7

for i in MyGen().by_seven( int(input('Please enter a number... ')) ):
    print(i)
