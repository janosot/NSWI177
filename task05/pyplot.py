#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

scores = []
tests = []
with open('data/tests.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] in tests:
           k = tests.index(row[0])
           if int(row[2]) > int(scores[k]):
                scores[k] = int(row[2])
        else:
            if row[2] <= '9' and row[2] >= '0':
                scores.append(int(row[2]))
                tests.append(row[0])

print(tests)
print(scores)
plt.bar(tests, scores)
plt.savefig('img/barplot.pdf')
