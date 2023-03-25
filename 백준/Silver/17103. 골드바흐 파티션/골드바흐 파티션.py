prime=[]
list1=[0]*1000001
for i in range(2,1000001):
    if list1[i]==0:
        prime.append(i)
        for j in range(2*i,1000001,i):
            list1[j]=1
for _ in range(int(input())):
    num=int(input())
    half=num//2
    cnt=0
    for i in prime:
        if(i>half):
            break
        if(not list1[num-i]):
            cnt+=1  
    print(cnt)