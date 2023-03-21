n,m=map(int,input().split())
list1=[i+1 for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    list1=list1[0:a-1]+list1[a-1:b][::-1]+list1[b:]
for i in range(len(list1)):
    print(list1[i], end=' ')