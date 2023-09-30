import sys

n = sys.stdin.readline()
stack1 = list(map(int,sys.stdin.readline().rstrip().split()))
stack2 = []
rank = 1

while stack1:
    if stack1[0] == rank:
        stack1.pop(0)
        rank+=1
        while stack2:
            if stack2[-1] == rank:
                stack2.pop()
                rank+=1
            else:
                break
    else:
        stack2.append(stack1.pop(0))

if stack2:
    print("Sad")
else:
    print("Nice")