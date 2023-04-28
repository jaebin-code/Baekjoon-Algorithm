import sys
input=sys.stdin.readline
n=int(input().rstrip())
stack=[]
list1=[]
flag=0
num=1
for _ in range(n):
    a=int(input().rstrip())
    while num<=a:
        stack.append(num)
        list1.append("+")
        num+=1
    if stack[-1]==a:
        stack.pop()
        list1.append("-")
    else:
        flag=1
if(flag==0):
    for i in list1:
        print(i)
else:
    print("NO")