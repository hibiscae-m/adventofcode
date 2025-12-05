#!/usr/bin/env python3

def loadFile(file_location:str):
    with open(file_location) as f:
        d = f.read()
        f.close()
    return d


def getPositions(coordinates, max_width, max_height):
    
    results = [[coordinates[0] - 1, coordinates[1] - 1],
              [coordinates[0] - 1, coordinates[1]],
              [coordinates[0] - 1, coordinates[1] + 1],
              [coordinates[0], coordinates[1] - 1],
              [coordinates[0], coordinates[1] + 1],
              [coordinates[0] + 1, coordinates[1] - 1],
              [coordinates[0] + 1, coordinates[1]],
              [coordinates[0] + 1, coordinates[1] + 1]
              ]
    
    final = []
    for result in results:
        if result[0] >= 0 and result[0] <= max_width and result[1] >= 0 and result[1] <= max_height:
            final.append(result)
    return final


def main():
    data = loadFile('data.txt')
    lines_loaded = data.split('\n')
    lines = []
    for line_loaded in lines_loaded:
        temp = []
        for char in line_loaded:
            temp.append(char)
        lines.append(temp)
    final_count = 0
    changed = True    

    rolls = []
    while changed:
        changed = False
        for i in range (0, len(lines)):
            for j in range(0, len(lines[i])):
                if lines[i][j] == '@':
                    available_pos = getPositions([i, j], len(lines) - 1, len(lines[i]) - 1)
                    count = 0
                    for position in available_pos:
                        if lines[position[0]][position[1]] == '@':
                            count += 1
                    if count < 4:
                        rolls.append([i, j])
                        final_count += 1
                        changed = True

        for roll in rolls:
            lines[roll[0]][roll[1]] = '.'
        rolls = []
    print(final_count)


if __name__ == '__main__':
    main()
