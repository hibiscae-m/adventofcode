#!/usr/bin/env python3

def loadFile(file_location:str):
    with open(file_location) as f:
        d = f.read()
        f.close()
    return d


def main():
    data = loadFile('data.txt')
    lines_loaded = data.split('\n')
    lines = []
    for line_loaded in lines_loaded:
        temp = []
        # elements = line_loaded.split()
        elements = list(line_loaded)
        for element in elements:
            temp.append(element)
        lines.append(temp)


    numbers = ''
    for i in range (len(lines[0]) - 1, -1, -1):
        number = ''
        # operation = lines[len(lines) - 1][i]
        for j in range(0, len(lines) - 1):
            number += lines[j][i]
        cleaned_number = number.strip()
        if cleaned_number.isdigit():
            numbers += cleaned_number + ' '
        else:
            numbers += '\n'

    operations = ''
    for i in range (len(lines[len(lines) - 1]) - 1, -1, -1):
        if lines[len(lines) - 1][i] != ' ':
            operations += lines[len(lines) - 1][i]

    data_num = numbers.split('\n')
    data_op = list(operations)

    final = 0
    for i in range(0, len(data_num)):
        temp = data_num[i].split()
        result = int(temp[0])
        for j in range(1, len(temp)):
            if data_op[i] == '+':
                result = result + int(temp[j])
            elif data_op[i] == '*':
                result = result * int(temp[j])
        final += result
    print(final)            

    ## Part One
    # final = 0
    # for i in range(0, len(lines[0])):
    #     result = int(lines[0][i])
    #     operation = lines[len(lines) - 1][i]
    #     for j in range(1, len(lines) - 1):
    #         # print('doing math for', result, operation, lines[j][i])
    #         if operation == '*':
    #             result = result * int(lines[j][i])
    #         elif operation == '+':
    #             result = result + int(lines[j][i])
    #     final += result
    # print(final)


if __name__ == '__main__':
    main()
