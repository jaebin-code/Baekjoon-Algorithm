row,col=map(int,input().split())
a=[]
b=[]
for i in range(row):
    a.append(list(map(int,input().split())))
for i in range(row):
    b.append(list(map(int,input().split())))
for i in range(row):
    for j in range(col):
        print(a[i][j]+b[i][j], end=' ')