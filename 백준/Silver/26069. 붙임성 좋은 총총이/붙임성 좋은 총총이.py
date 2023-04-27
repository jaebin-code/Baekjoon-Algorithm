num=int(input())
dic={"ChongChong":1}
cnt=0
for _ in range(num):
    n,k=input().split()
    if n not in dic:
        dic[n]=0
    if k not in dic:
        dic[k]=0
    if dic[n]==1 or dic[k]==1:
        dic[n]=1
        dic[k]=1
for i,j in dic.items():
    if j==1:
        cnt+=1
print(cnt)