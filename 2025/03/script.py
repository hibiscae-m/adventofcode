#!/usr/bin/env python3

def loadFile(file_location:str):
    with open(file_location) as f:
        d = f.read()
        f.close()
    return d


def main():
    data = loadFile('data.txt')
    batteries = data.split('\n')
    final = 0
    digit_wanted = 12

    for batterie in batteries:
        count = 0
        buffer = []

        while count < len(batterie):
            searched_number = 9
            for i in range (0, len(batterie)):
                buffer.append(batterie[i] + ',' + str(i))
                count += 1
            searched_number -= 1

        digits = len(buffer)
        start_index = 0
        while digits > digit_wanted:
            found = False
            for i in range (0, digits - 1):
                if int(str(buffer[i]).split(',')[0]) < int(str(buffer[i+1]).split(',')[0]):
                    move_element = buffer.pop(i)
                    buffer.append(move_element)
                    digits -= 1
                    found = True
                    break
            if not found:
                start_index += 1
                digits -= 1

        to_delete = len(buffer) - digit_wanted
        del buffer[-to_delete:]
        
        for i in range (0, len(buffer)):
            min_idx = int(str(buffer[i]).split(',')[1])
            for j in range (i + 1, len(buffer)):
                if int(str(buffer[j]).split(',')[1]) < int(min_idx):
                    min_idx = int(str(buffer[j]).split(',')[1])
                    buffer[i], buffer[j] = buffer[j], buffer[i]
                            
        result = ''
        for element in buffer:
            result = result + str(element).split(',')[0]
        final += int(result)

    print(final)


if __name__ == '__main__':
    main()
