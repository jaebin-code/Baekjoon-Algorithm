import sys
input=sys.stdin.readline
n=int(input().rstrip())
num=list(map(int,input().split()))
op=list(map(int,input().split()))
maxn=-1e9
minn=1e9

def dfs(depth,answer,plus,minus,mul,div):
    global maxn,minn
    if len(num)==depth:
        maxn=max(maxn,answer)
        minn=min(minn,answer)
        return
    if plus:
        dfs(depth+1,answer+num[depth],plus-1,minus,mul,div)
    if minus:
        dfs(depth+1,answer-num[depth],plus,minus-1,mul,div)
    if mul:
        dfs(depth+1,answer*num[depth],plus,minus,mul-1,div)
    if div:
        dfs(depth+1,int(answer/num[depth]),plus,minus,mul,div-1)
dfs(1,num[0],op[0],op[1],op[2],op[3])            
print(maxn)
print(minn)