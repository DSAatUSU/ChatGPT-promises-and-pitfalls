inputString = input('Enter a string to analyze: ').lower()
targetLetter = input('Enter a letter to check for occurrences: ').lower()


def count(string, target):
    i = 0
    while i < len(string):
        if string[i] == target:
            return 1 + count(string[i+1:], target)
        i += 1
    return 0


print(count(inputString, targetLetter))
