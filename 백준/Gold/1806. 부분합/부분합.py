import sys
input=sys.stdin.readline

n,k=map(int,input().split())

seq=list(map(int,input().split()))

pointer1=0
pointer2=0
answer=1e9
sum1=0
while True:
    if sum1>=k:
        if answer>(pointer2-pointer1):
            answer=pointer2-pointer1
        sum1-=seq[pointer1]
        pointer1+=1
    elif pointer2==n:
        break
    else:
        sum1+=seq[pointer2]
        pointer2+=1
        
    if answer==1:
        break
if answer==1e9:
    print(0)
else:
    print(answer)