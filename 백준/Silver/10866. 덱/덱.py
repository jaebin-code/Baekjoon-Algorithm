import sys
from collections import deque
input=sys.stdin.readline
num=int(input())
que=deque([])
for _ in range(num):
    word=input().split()
    if(word[0]=="push_front"):
        que.appendleft(word[1])
    elif(word[0]=="push_back"):
        que.append(word[1])
    elif(word[0]=="pop_front"):
        if(len(que)==0):
            print(-1)
        else:
            print(que.popleft())
    elif(word[0]=="pop_back"):
        if(len(que)==0):
            print(-1)
        else:
            print(que.pop())
    elif(word[0]=="size"):
        print(len(que))
    elif(word[0]=="empty"):
        if(len(que)==0):
            print(1)
        else:
            print(0)
    elif(word[0]=="front"):
        if(len(que)==0):
            print(-1)
        else:
            print(que[0])
    elif(word[0]=="back"):
        if(len(que)==0):
            print(-1)
        else:
            print(que[-1])