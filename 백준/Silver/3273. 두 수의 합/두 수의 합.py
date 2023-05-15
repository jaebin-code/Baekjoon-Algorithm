import sys
input=sys.stdin.readline

n=int(input().rstrip())
sol=list(map(int,input().split()))
num=int(input().rstrip())

sol.sort()
idx1=0
idx2=n-1
cnt=0
while idx1<idx2:
    sumnum=sol[idx1]+sol[idx2]
    if sumnum==num:
        cnt+=1
        idx1+=1
        idx2-=1
    elif sumnum<num:
        idx1+=1
    else:
        idx2-=1
print(cnt)