import sys
input=sys.stdin.readline
seq=[]
def dfs(n,m,start):
    if len(seq)==m:
        print(" ".join(map(str,seq)))
        return 0
    for i in range(start,n+1):
        if i not in seq:
            seq.append(i)
            dfs(n,m,i+1)
            seq.pop()
n,m=map(int,input().split())
dfs(n,m,1)