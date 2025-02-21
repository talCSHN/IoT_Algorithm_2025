import random

row, col = 5, 5
goldMaze = [[random.randint(0, 5) for _ in range(row)] for _ in range(col)]
# print(goldMaze)

def printMaze(arr):
    for i in range(row):
        for k in range(col):
            print(f'{arr[i][k]:3d}', end=' ')
        print()
    print()

def growRich():
    memo = [[0 for _ in range(col)] for _ in range(row)]
    memo[0][0] = goldMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, row):
        rowSum += goldMaze[0][i]
        memo[0][i] = rowSum

    colSum = memo[0][0]
    for i in range(1, col):
        colSum += goldMaze[i][0]
        memo[i][0] = colSum
    
    for r in range(1, row):
        for c in range(1, col):
            if memo[r][c-1] > memo[r-1][c]:
                memo[r][c] = memo[r][c-1] + goldMaze[r][c]
            else:
                memo[r][c] = memo[r-1][c] + goldMaze[r][c]
    
    resultValue =  memo[row-1][col-1]

    print('##############')
    printMaze(memo)
    rrow, ccol = row-1, col-1

    memo[rrow][ccol] = 0
    while rrow != 0 or ccol != 0:
        if rrow-1 >= 0 and ccol-1 >= 0:
            if memo[rrow-1][ccol] > memo[rrow][ccol-1]:
                rrow -= 1
            else:
                ccol -= 1
        elif rrow-1 < 0 and ccol-1 >= 0:
            ccol -= 1
        else:
            rrow -= 1
        memo[rrow][ccol] = 0
    
    print('######### 황금 미로 길 ########')
    printMaze(memo)

    return resultValue

maxGold = growRich()
print(f'최대 황금 갯수 : {maxGold}')