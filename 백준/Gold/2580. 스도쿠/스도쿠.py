import sys
input=sys.stdin.readline
blank=[]
sudoku=[]
for _ in range(9):
    sudoku.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if(sudoku[i][j]==0):
            blank.append((i,j))
def rowcheck(x,row):
    for i in range(9):
        if x== sudoku[row][i]:
            return False
    return True

def colcheck(x,col):
    for i in range(9):
        if x==sudoku[i][col]:
            return False
    return True

def three(result,x,y):
    a=(x//3)*3
    b=(y//3)*3
    for i in range(a,a+3):
        for j in range(b,b+3):
            if(sudoku[i][j]==result):
                return False
    return True

def dfs(n):
    if n==len(blank):
        for i in sudoku:
            for j in i:
                print(j,end=" ")
            print("")
        exit(0)
    for j in range(1,10):
        x=blank[n][0]
        y=blank[n][1]
        if rowcheck(j,x) and colcheck(j,y) and three(j,x,y):
            sudoku[x][y]=j
            dfs(n+1)
            sudoku[x][y]=0
dfs(0)