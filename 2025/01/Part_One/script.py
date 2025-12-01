#!/bin/env python

position = 50
password = 0
first = []
second = []

def rotate(pos:int, direction:str, value:int):
    if direction == 'L':
        value = value * -1
    pos += value
    while pos > 99:
        pos -= 100
    while pos < 0:
        pos += 100
    return pos

with open('data.txt') as f:
    d = f.read().split('\n')
    for line in d:
        first.append(line[:1]) 
        second.append(line[1:])
    f.close()

for i in range(len(first)):
    position = rotate(position, first[i], int(second[i]))
    print(position)
    if position == 0:
        password += 1

print('password = ', password)
