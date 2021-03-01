# Nicolas Campero
# 1856853

import csv
file = 'input1.csv'
frequency = {}

with open(file, 'r') as csvfile:
    csvfile = csv.reader(csvfile)
    for row in csvfile:
        for word in row:
            if word not in frequency.keys():
                frequency[word] = 1
            else:
                frequency[word] = frequency[word] + 1
for i in frequency.keys():
    print(i,frequency[i])