n,m=map(int,input().split())
list1=[]
list2=[]
for _ in range(0,n):
    list1.append(input())

for a in range(0,n-7):
    for i in range(0,m-7):
        count1=0
        count2=0  
        for b in range(a,a+8):
            for j in range(i,i+8): 
                if (b+j)%2==0:
                    if list1[b][j]=='W':
                        count1+=1
                    if list1[b][j]=='B':
                        count2+=1
                else:
                    if list1[b][j]=='B':
                        count1+=1
                    if list1[b][j]=='W':
                        count2+=1
        list2.append(count1)
        list2.append(count2)
print(min(list2))