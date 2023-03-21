length=int(input())
list1=list(map(int,input().split()))
answer=int(input())
list1.sort()
cnt=0
for i in range(len(list1)):
    if(list1[i]==answer):
        cnt+=1
    if(list1[i]>answer):
        break
print(cnt)