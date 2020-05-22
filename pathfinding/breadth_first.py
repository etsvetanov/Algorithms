from queue import Queue

class Node:
    def __self__(self):
        self.state = ''

class Grid:
    def __init__(self, size):
        self.grid = [[i for i in range(size)] for i in range(size)]

    def __str__(self):
        return '\n'.join(['  '.join([str(i) for i in r]) for r in self.grid])

a = Grid(10)

print(a)

