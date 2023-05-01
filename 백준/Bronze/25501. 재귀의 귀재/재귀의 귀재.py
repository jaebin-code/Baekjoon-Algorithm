import sys
input=sys.stdin.readline
n=int(input())

def recursion(str,l,r,num):
    if(l>=r):
        return 1,num+1
    elif str[l]!=str[r]:
        return 0,num+1
    else:
        return recursion(str,l+1,r-1,num+1)
for _ in range(n):
    a=input().rstrip()
    b,c=recursion(a,0,len(a)-1,0)
    print(b,c)