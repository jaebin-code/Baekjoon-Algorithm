import sys
from collections import deque
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    signal=0
    word=list(input().rstrip())
    num=int(input().rstrip())
    b=deque(input().rstrip()[1:-1].split(','))
    rcnt=0
    if(num==0):
        b=deque()
    for i in word:
        if i=="R":
            rcnt+=1
        else:
            if len(b)==0:
                print("error")
                signal=1
                break
            else:
                if rcnt%2==0:
                    b.popleft()
                else:
                    b.pop()
    if signal==0:
        if rcnt%2==0:
            print("["+",".join(b)+"]")
        else:
            b.reverse()
            print("["+",".join(b)+"]")