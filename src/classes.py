class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def copyPoint(self, point1):
        self.x = point1.x
        self.y = point1.y

    def display_point(self):
        print(f"{self.y + 1}, {self.x + 1}")

class Matrix:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.el = [[val for i in range(col)] for j in range(row)]
        self.pos = Point(0,0)
        self.path = []

    def copyMatrix(self, matrix1):
        self.row = matrix1.row
        self.col = matrix1.col
        self.pos = matrix1.pos
        self.path = [Point(0, 0) for  i in range(len(matrix1.path))]
        for i in range(len(matrix1.path)):
            self.path[i].copyPoint(matrix1.path[i])
        self.el = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.el[i][j] = matrix1.el[i][j]

    def display(self):
        for i in range(self.row):
            print("[", end="")
            for j in range(self.col):
                print(self.el[i][j], end = " ")
            print("]")