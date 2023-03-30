n,k=map(int,input().split())
share=-1
result=''
list1='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while (n!=0):
    result=list1[n%k]+result
    n=n//k
print(result)