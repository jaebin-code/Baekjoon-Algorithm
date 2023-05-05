import sys
input=sys.stdin.readline
seq=[]
def dfs(n,m,start):
    if len(seq)==m:
        print(" ".join(map(str,seq)))
        return 0
    for i in range(start,n+1):
        seq.append(i)
        dfs(n,m,i)
        seq.pop()
n,m=map(int,input().split())
dfs(n,m,1)