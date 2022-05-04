table = [['apples', 'orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

strName = ''
maxLen = -1
# Find longest string in table
for y in range(len(table[0])):

    for x in range(len(table)):
        strName = table[x][y]
        if len(strName) > maxLen:
            maxLen = len(strName) + 1

# Print table
for y in range(len(table[0])):

    newTable = ''
    for x in range(len(table)):
        newTable = newTable + (table[x][y].ljust(maxLen))
    print(newTable)
