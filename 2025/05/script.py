#!/usr/bin/env python3

def loadFile(file_location:str):
    with open(file_location) as f:
        d = f.read()
        f.close()
    return d


def partOne():
    data = loadFile('data.txt')
    range_ids, ingredient_ids = data.split('\n\n')[0].split('\n'), data.split('\n\n')[1].split('\n')
    fresh = []

    for i in range (0, len(ingredient_ids) - 1):
        for range_id in range_ids:
            start, end = int(range_id.split('-')[0]), int(range_id.split('-')[1])
            if int(ingredient_ids[i]) >= start and int(ingredient_ids[i]) <= end:
                fresh.append(ingredient_ids[i])
                break

    print(len(fresh))

def partTwo():
    data = loadFile('data.txt')
    fresh_ids = data.split('\n\n')[0].split('\n')
    moved = True

    # Conversation des valeurs en tableau imbriqué
    for i in range (0, len(fresh_ids)):
        fresh_ids[i] = [int(str(fresh_ids[i]).split('-')[0]), int(str(fresh_ids[i]).split('-')[1])]

    # Tri par ordre de début de range
    while moved:
        moved = False
        for i in range (0, len(fresh_ids) - 1):
            for j in range(i + 1, len(fresh_ids)):
                if fresh_ids[i][0] > fresh_ids[j][0] or (fresh_ids[i][0] == fresh_ids[j][0] and fresh_ids[i][1] > fresh_ids[j][1]):
                    fresh_ids[i], fresh_ids[j] = fresh_ids[j], fresh_ids[i]
                    moved = True

    # Suppression des valeurs inutiles (ex: [10, 14], [12, 18] deviendraient [10, 18])
    index = 0
    while (index < len(fresh_ids) - 1):
        if fresh_ids[index][1] + 1 >= fresh_ids[index + 1][0]:
            if not fresh_ids[index][1] > fresh_ids[index + 1][1]:
                fresh_ids[index][1] = fresh_ids[index + 1][1]
            fresh_ids.pop(index + 1)
            moved = True
        else:
            index += 1

    # Calcul de l'ensemble
    result = 0
    for fresh_range in fresh_ids:
        result += fresh_range[1] - fresh_range[0] + 1    

    print(result)

if __name__ == '__main__':
    partTwo()
