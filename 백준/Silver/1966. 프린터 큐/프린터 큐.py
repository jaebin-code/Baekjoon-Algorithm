import sys
from collections import deque
input=sys.stdin.readline
num=int(input())
for _ in range(num):
    n,k=map(int,input().split())
    que=deque(list(map(int,input().split())))
    cnt=0
    while que:
        maxnum=max(que)
        front=que.popleft()
        k-=1
        if maxnum==front:
            cnt+=1
            if(k<0):
                print(cnt)
                break
        else:
            que.append(front)
            if k<0:
                k=len(que)-1