import csv

examplefile = open('example.csv')

exampleReader = csv.reader(examplefile)

exampleData = list(exampleReader)

print(exampleData)