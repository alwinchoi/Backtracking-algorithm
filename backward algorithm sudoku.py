import numpy as np
grid = [[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]]

def algorithm(y,x,no):
    global grid
    for i in range(0,9):
        if grid[y][i] == no:
            return False
    for i in range(0,9):
        if grid[i][x] == no:
            return False
    testy = (y//3)*3
    testx = (x//3)*3
    for tempy in range(testy, testy+3):
        for tempx in range(testx, testx+3):
            if grid[tempy][tempx] == no:
                return False
    return True
        
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for number in range(1,10):
                    if algorithm(y,x,number):
                        grid[y][x] = number
                        solve() #this would work if there is any number left, recursion\
                        grid[y][x] = 0
                return #once it's done or has to backtrack but if you are done, no number will be avaliable then it just stops
    print(np.matrix(grid))
    input("more?")

solve()




