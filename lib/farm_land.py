import numpy as np, random as r

# This program will create and return a 2D array with 0's and 1's.
#  Dimensions will be random, as will the determination of an item being 0 or 1

def createMatrix():
    columns = r.randint(15,60)
    rows = r.randint(15,40)
    matrix = np.random.randint(0, 2, size=(rows, columns))
    return matrix


def findSqrDim(matrix, startRowIndex, startColIndex):   
    maxRow, maxCol = matrix.shape
    curentRowIndex, currentColIndex = startRowIndex, startColIndex
    dimensions = 1
    firstIteration = True
    valid = True

    while valid:
        if (curentRowIndex > maxRow - 1) or (currentColIndex > maxCol - 1):
            valid = False
        elif matrix[curentRowIndex][currentColIndex] != 1:
            valid = False
        elif firstIteration:
            firstIteration = False
            curentRowIndex += 1 
            currentColIndex += 1
            continue
        else:
            checkRow = matrix[curentRowIndex][startColIndex:currentColIndex]
            checkCol = matrix[startRowIndex:curentRowIndex]
            for land in checkRow:
                if land != 1:
                    valid = False
                    break
            for row in checkCol:
                if row[currentColIndex] != 1:
                    valid = False
                    break
            
            if not valid:
                break
            dimensions += 1 
            curentRowIndex += 1 
            currentColIndex += 1
    
    return dimensions


def findFarmableLand(matrix):
    farmableLand = {}
    landCount = 0
    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[0])):
            if matrix[rowIndex][colIndex] == 1:
                farmableLand[f'land {landCount + 1}'] = findSqrDim(matrix, rowIndex, colIndex)
                landCount += 1

    return farmableLand


def findLargestSqr(dic):
    largestSqr = [0,0]
    for dimension in dic.values():
        if dimension > largestSqr[0]:
            largestSqr[0] = dimension
            largestSqr[1] = dimension
    return largestSqr


