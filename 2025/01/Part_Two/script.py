#!/bin/env python

position = 50
password = 0
first = []
second = []

def rotate(pos:int, value:int):
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
    if first[i] == 'L':
        value = int(second[i]) * -1
    else: 
        value = int(second[i])

    if (position + value) < 0:
        if position == 0:
            if value < -99:
                password += int(str(abs((position + value) / 100)).split('.')[0])
        else:
            password += (1 + int(str(abs((position + value) / 100)).split('.')[0]))

    elif (position + value) > 100:
        password += int(str((position + value) / 100).split('.')[0])

    elif (position + value) == 100 or (position + value) == 0:
        password += 1

    position = rotate(position, value)

print('password = ', password)
