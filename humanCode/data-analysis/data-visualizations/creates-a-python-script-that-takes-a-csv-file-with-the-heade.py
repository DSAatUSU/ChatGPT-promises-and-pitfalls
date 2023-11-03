import csv
from matplotlib import pyplot

csvfile = open("tests_data/histogramData.csv")
header = input("Specify the header over which to create the histogram (must be all integer data): ")

data = [int(row[header]) for row in csv.DictReader(csvfile)]

pyplot.hist(data)
pyplot.show()



