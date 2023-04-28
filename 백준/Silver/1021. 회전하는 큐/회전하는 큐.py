import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
que=deque([])
for i in range(1,n+1):
    que.append(i)
list1=list(map(int,input().split()))
cnt=0
for i in list1:
    while True:
        if que[0]==i:
            que.popleft()
            break
        if que.index(i)<len(que)/2:
            while que[0]!=i:
                que.append(que.popleft())
                cnt+=1
        else:
            while que[0]!=i:
                que.appendleft(que.pop())
                cnt+=1
print(cnt)