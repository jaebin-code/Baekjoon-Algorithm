import sys
input=sys.stdin.readline

n=int(input().rstrip())
num=list(map(int,input().split()))
num.sort()


idx1=num[0]
idx2=num[n-1]
left=0
right=len(num)-1
answer=abs(num[0]+num[len(num)-1])
while left<right:
    sumnum=num[left]+num[right]
    if answer>abs(sumnum):
        answer=abs(sumnum)
        idx1=num[left]
        idx2=num[right]
        if answer==0:
            break
    if sumnum<0:
        left+=1
    else:
        right-=1
    
print(idx1,idx2)