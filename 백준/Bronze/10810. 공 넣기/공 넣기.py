n,m=map(int,input().split())
list1=[0]*n
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        list1[j]=c
for i in range(len(list1)):
    print(list1[i], end=" ")