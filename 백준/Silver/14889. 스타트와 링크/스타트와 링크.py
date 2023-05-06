import sys
input=sys.stdin.readline
n=int(input().rstrip())
num=[]
for _ in range(n):
    num.append(list(map(int,input().split())))

def dfs(depth,idx):
    global minn
    if depth==n//2:
        num1=0
        num2=0
        for i in range(n):
            for j in range(n):
                if checklist[i]==True and checklist[j]==True:
                    num1+=num[i][j]
                elif checklist[i]==False and checklist[j]==False:
                    num2+=num[i][j]
        minn=min(minn,abs(num1-num2))
        return
    for i in range(idx,n):
            checklist[i]=True
            dfs(depth+1,i+1)
            checklist[i]=False

minn=1e9
checklist=[False]*n
dfs(0,0)
print(minn)
