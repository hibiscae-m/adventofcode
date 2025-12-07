#!/usr/bin/env python3

# Part Two doesn't work :(

class Spliter:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.left_closed = False
        self.right_closed = False
        self.left_child = None
        self.right_child = None
        self.paths = 0

    def close(self, direction):
        if direction == 'Left':
            self.left_closed = True
        elif direction == 'Right':
            self.right_closed = True

    def isClosed(self):
        if self.left_closed and self.right_closed:
            return True
        return False
    
    def open(self):
        self.left_closed = False
        self.right_closed = False

    def getCoordinates(self):
        return self.coordinates
    
    def registerChild(self, child, direction):
        if direction == 'Left':
            if self.left_child == None:
                self.left_child = child
        elif direction == 'Right':
            if self.right_child == None:
                self.right_child = child
            
    def getChildren(self):
        temp = []
        if self.left_child != None:
            temp.append(self.left_child)
        if self.right_child != None:
            temp.append(self.right_child)
        return temp

    def tracePath(self):
        while not self.isClosed():

            if self.left_child != None:
                if not self.left_child.isClosed():
                    self.paths += self.left_child.tracePath()
                else:
                    self.close('Left')

            if self.right_child != None:
                if not self.right_child.isClosed():
                    self.paths += self.right_child.tracePath()
                else:
                    self.close('Right')

            if self.left_child == None:
                self.paths += 1
                self.close('Left')
            if self.right_child == None:
                self.paths += 1
                self.close('Right')

            if self.isClosed():
                if self.left_child != None:
                    self.left_child.open()
                if self.right_child != None:
                    self.right_child.open()

        return self.paths
        
        
            


def loadFile(file_location:str):
    with open(file_location) as f:
        d = f.read()
        f.close()
    return d


def partOne(data):
    count = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == 'S' or data[i][j] == '|':
                if i + 1 <= len(data)- 1:
                    if data[i + 1][j] == '.':
                        data[i + 1][j] = '|'
                    elif data[i + 1][j] == '^':
                        count += 1
                        if j - 1 >= 0:
                            data[i + 1][j - 1] = '|'
                        if j + 1 <= len(data[i]) - 1:
                            data[i + 1][j + 1] = '|'    
    print(count)

def partTwo(data):
    count = 0
    spliters = []
    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            if data[i][j] == '^':
                spliters.append(Spliter([i, j]))
    for first in spliters:
        for second in spliters:
            if first != second:
                for i in range (first.getCoordinates()[0], len(data)):
                    if second.getCoordinates() == [i, first.getCoordinates()[1] - 1]:
                        first.registerChild(second, 'Left')
                        break
                for i in range (first.getCoordinates()[0], len(data)):
                    if second.getCoordinates() == [i, first.getCoordinates()[1] + 1]:
                        first.registerChild(second, 'Right')
                        break
    for spliter in spliters:
        print('####')
        print('spliter in', spliter.getCoordinates())
        for child in spliter.getChildren():
            print('child in', child.getCoordinates())

    print(spliters[0].tracePath())





def main():
    # Data in two entries array
    loaded_data = loadFile("data_short.txt").split('\n')
    data = []
    for line in loaded_data:
        temp = []
        for char in line:
            temp.append(char)
        data.append(temp)
    
    partTwo(data)

if __name__ == '__main__':
    main()
