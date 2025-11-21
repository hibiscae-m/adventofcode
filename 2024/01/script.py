#!/usr/bin/env python3

first = []
second = []
math = []
result = 0

with open('data.txt') as f:
    d = f.read().split('\n')
    for line in d:
        first.append(line.split()[0]) 
        second.append(line.split()[1])
    f.close()

first.sort()
second.sort()

for i in range(len(first)):
    math.append(abs(int(first[i]) - int(second[i])))

for el in math:
    result = result + el

print(result)
