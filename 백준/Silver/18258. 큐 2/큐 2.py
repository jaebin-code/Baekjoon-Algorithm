import sys
from collections import deque
input=sys.stdin.readline
n=int(input().rstrip())
que=deque([])
for _ in range(n):
    word=input().split()
    if word[0]=="push":
        que.append(int(word[1]))
    elif word[0]=="front":
        if(len(que)==0):
            print(-1)
        else:
            print(que[0])
    elif word[0]=="back":
        if(len(que)==0):
            print(-1)
        else:
            print(que[-1])
    elif word[0]=="empty":
        if(len(que)==0):
            print(1)
        else:
            print(0)
    elif word[0]=="size":
        print(len(que))
    elif word[0]=="pop":
        if(len(que)==0):
            print(-1)
        else:
            print(que.popleft())