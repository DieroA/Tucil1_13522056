from classes import Matrix, Point

def markEl(matrix, point):
    copiedMatrix = Matrix(1, 1, 1)
    copiedMatrix.copyMatrix(matrix)

    copiedMatrix.path.append(point)
    copiedMatrix.pos = point
    copiedMatrix.el[point.x][point.y] = "~~"
    
    return copiedMatrix

def gerak(matrix, point, isVertical):
    arah_gerak = []
    if isVertical:
        for i in range(matrix.row):
            if matrix.el[i][point.y] != "~~":
                arah_gerak.append(Point(i, point.y))
    else:
        for i in range(matrix.col):
            if matrix.el[point.x][i] != "~~":
                arah_gerak.append(Point(point.x, i))
    return arah_gerak 

def searchMatrix(matrix, buffer_size):
    matrices = []
    for i in range(0, len(matrix.el[0])):
        newMatrix = markEl(matrix, Point(0, i))
        matrices.append(newMatrix)
    
    isVertical = True
    for i in range(buffer_size - 1):
        matrices_new = []
        for j in matrices:
            gerakan = gerak(j, j.pos, isVertical)
            for k in gerakan:
                new_matrix = markEl(j, k)
                matrices_new.append(new_matrix)

        matrices = matrices_new        
        # Flip isVertical
        isVertical = not isVertical

    return matrices

def pointToToken(point, matrix):
    return matrix.el[point.x][point.y]