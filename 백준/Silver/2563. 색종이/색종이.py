list1=[[0]*101 for _ in range(101)]

for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            list1[a+i][b+j]=1
cnt=0
for i in range(101):
    cnt+=list1[i].count(1)
print(cnt)