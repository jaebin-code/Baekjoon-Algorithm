a,b=map(int,input().split())
n=1
cnt=0
while (n<=a):
    if(a%n==0):
        cnt+=1
    
    if(b==cnt):
        print(n)
        break
    if(a==n and cnt<b):
        print(0)
    n+=1