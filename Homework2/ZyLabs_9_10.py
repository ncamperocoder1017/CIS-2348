# Nicolas Campero
# 1856853

import csv
file = 'input1.csv'
word_freq = {}

with open(file, 'r') as csvfile:
    csvfile = csv.reader(csvfile)
    for row in csvfile:
        for word in row:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] = word_freq[word] + 1
for i in word_freq.keys():
    print(i, word_freq[i])
