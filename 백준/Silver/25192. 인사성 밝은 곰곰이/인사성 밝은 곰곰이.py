num=int(input())
dic={}
cnt=0
for _ in range(num):
    s=input()
    if s=="ENTER":
        dic={}
    elif s not in dic:
        cnt+=1
        dic[s]=1
        
print(cnt)