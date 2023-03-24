a,b=map(int,input().split())
x,y=min(a,b),max(a,b)
while(x!=0):
    x,y=y%x,x
print(int(a*b/y))