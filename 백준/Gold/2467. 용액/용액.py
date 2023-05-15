import sys
input=sys.stdin.readline

n=int(input().rstrip())
sol=list(map(int,input().split()))

idx1=0
idx2=n-1
result=abs(sol[0]+sol[n-1])
idx3=0
idx4=n-1
while idx1<idx2:
    sumnum=sol[idx1]+sol[idx2]
    if result>abs(sumnum):
        result=abs(sumnum)
        idx3=idx1
        idx4=idx2
        if result==0:
            break
    if sumnum>0:
        idx2-=1
    else:
        idx1+=1
print(sol[idx3],sol[idx4])