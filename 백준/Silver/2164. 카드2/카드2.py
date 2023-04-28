import sys
from collections import deque
input=sys.stdin.readline
n=int(input().rstrip())
que=deque([])
for i in range(1,n+1):
    que.append(i)
while len(que)!=1:
    que.popleft()
    que.append(que.popleft())
print(que[0])