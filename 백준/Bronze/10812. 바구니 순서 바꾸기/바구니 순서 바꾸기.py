a,b=map(int,input().split())

list1=[i+1 for i in range(a)]

for i in range(b):
    i,j,k=map(int,input().split())
    i,j,k=i-1,j-1,k-1
    list1=list1[:i]+list1[k:j+1]+list1[i:k]+list1[j+1:]
for i in range(len(list1)):
    print(list1[i],end=' ')