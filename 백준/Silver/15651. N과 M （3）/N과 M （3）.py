import sys
input=sys.stdin.readline
seq=[]
def dfs(n,m):
    if len(seq)==m:
        print(" ".join(map(str,seq)))
        return 0
    for i in range(1,n+1):
        seq.append(i)
        dfs(n,m)
        seq.pop()
n,m=map(int,input().split())
dfs(n,m)