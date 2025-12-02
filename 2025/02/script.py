#!/usr/bin/env python3

def hasOccurences(string:str, string_to_find:str):
    separate_string = [string[i:i+len(string_to_find)] for i in range(0, len(string), len(string_to_find))]
    for sequence in separate_string:
        if sequence != string_to_find:
            return False
    return True


def main():

    data =[]
    results = []

    with open('data.txt') as f:
        d = f.read().split(',')
        for w in d:
            data.append(w) 
        f.close()

    for numbers in data:
        first = str(numbers).split('-')[0]
        second = str(numbers).split('-')[1]
        for number in range (int(first), int(second) + 1):

            nb_of_digit = len(str(number))

            divisors = []
            for i in range (1, nb_of_digit):
                if (nb_of_digit % i == 0):
                    divisors.append(i)

            for divisor in divisors:
                if hasOccurences(str(number), str(number)[:divisor]):
                    results.append(number)
                    break

            ###
            # Part One
            ###
            # divisor = int(len(str(number)) / 2)
            # if hasOccurences(str(number), str(number)[:divisor]):
            #         results.append(number)

    final = 0
    for result in results:
        final += result
    print(final)

if __name__ == '__main__':
    main()
