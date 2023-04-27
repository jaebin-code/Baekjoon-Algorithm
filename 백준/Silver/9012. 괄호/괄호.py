
import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    b=input().rstrip()
    stack=list(b)
    cnt=0
    idx=0
    for i in stack:
        if i=='(':
            cnt+=1
        else:
            cnt-=1
        if(cnt<0):
            break
        idx+=1
    if(cnt==0):
        print("YES")
    else:
        print("NO")