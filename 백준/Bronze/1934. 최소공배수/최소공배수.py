length=int(input())
for i in range(length):
    a,b=map(int,input().split())
    x,y=min(a,b),max(a,b)
    while(x!=0):
        y,x=x,y%x
    print(int(a*b/y)) 