import numpy

string = input("Please input the string you would like to analyze: ")
if (string == ''):
    print("String must be non-empty.")
    exit(1)

strings = {}
for word in string.split():
    if word in strings:
        strings[word] += 1
    else:
        strings[word] = 1
words = len(string.split())
dict_vals = numpy.fromiter([x/words for x in strings.values()], dtype=float)
std_dev = numpy.std(dict_vals)
mean = numpy.std(dict_vals)

print("Statistically Significant Words:")
for word in strings:
    percent = strings[word]/words
    if abs(percent - mean) > std_dev:
        print(word)

