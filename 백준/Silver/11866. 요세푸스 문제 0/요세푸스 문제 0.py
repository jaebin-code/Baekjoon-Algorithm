import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,(input().split()))
que=deque([])
list1=[]
for i in range(1,n+1):
    que.append(i)
while que:
    for i in range(k-1):
        que.append(que.popleft())
    list1.append(que.popleft())
print("<",end="")
for i in range(n-1):
    print(str(list1[i])+",",end=" ")
print(str(list1[-1])+">")
