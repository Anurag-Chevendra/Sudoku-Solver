import random


def solveSudoku(grid, x, y):
    if(grid[x][y]==0):
        for i in range(1, 10):
            if (checkX(grid, i, x) and checkY(grid, i, y) and checkBox(grid, x, y, i)):
                grid[x][y] = i
                if 8 > y >= 0:
                    solveSudoku(grid, x, y + 1)
                elif x == 8 and y == 8:
                        Printgrid(grid)
                elif y == 8:
                    solveSudoku(grid, x + 1, 0)
        grid[x][y] = 0
    else:
        if y==8 and x==8 :
                Printgrid(grid)
        elif y==8 :
            solveSudoku(grid , x+1 , 0)
        elif 8>y>=0 :
            solveSudoku(grid , x , y+1)
def checkX(grid,num,row):
    c=0
    for i in range(9):
        if(grid[row][i]==num):
            c=1
            break
        else:
            c=0
    if(c==1):
        return False
    else:
        return True
def checkY(grid,num,col):
    c = 0
    for i in range(9):

        if grid[i][col] == num:
            c = 1
            break
        else:
            c = 0
    if (c == 1):
        return False
    else:
        return True
def checkBox(grid,row,col,num):
    c=0
    pointerX=0
    pointerY=0
    if 2 >= row >= 0:
        pointerX=0
    elif 3 <= row <= 5:
        pointerX=3
    elif 6 <= row <= 8:
        pointerX=6

    if 2 >= col >= 0:
        pointerY=0
    elif 3 <= col <= 5:
        pointerY=3
    elif 6 <= col <= 8:
        pointerY=6

    for x in range(pointerX,pointerX+3):
        for y in range(pointerY,pointerY+3):
            if(grid[x][y]==num):
                c=1

    if(c==1):
        return False
    else:
        return True

def MakeSudoku():

    Grid = [[0 for x in range(9)] for y in range(9)]
    print("Do you wish to input the Grid data ?")
    print("         enter 1 for : yes")
    print("         enter 2 for : no")
    choice=input()
    if(choice=="1"):
        ss=""
        for i in range(9):
            for j in range(9):
                    ss = ss + " (" + str(i) + "," + str(j) + ")" + " |"
            print("|"+ss)
            print("")
            ss=""

        print("enter elements one by one")
        for i in range(9):
            for j in range(9):
                print("("+str(i)+","+str(j)+") :")
                Grid[i][j] = int(input())
    else:
        for i in range(9):
            for j in range(9):
                Grid[i][j] = 0

            # The range here is the amount
            # of numbers in the grid
        for i in range(5):
            # choose random numbers
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
            while (not CheckValid(Grid, row, col, num) or Grid[row][col] != 0):  # if taken or not valid reroll
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            Grid[row][col] = num;

    Printgrid(Grid)
    print("do you want a solution?")
    option = int(input("      1)Yes  2)No  :"))
    print("NOTE: THERE MIGHT BE MORE THAN ONE SOLUTION!")
    if (option == 1):

        solveSudoku(Grid,0,0)


def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)


#     |-----------------------------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |-----------------------------|

def CheckValid(Grid, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if (Grid[rowsection * 3 + x][colsection * 3 + y] == num):
                valid = False
    return valid


MakeSudoku()
