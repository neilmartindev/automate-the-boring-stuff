import csv
from doctest import Example

exampleFile = open('example.csv')

exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    
    