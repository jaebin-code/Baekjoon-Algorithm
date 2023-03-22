list1=[]

for _ in range(5):
    list1.append(list(input().split()))
for i in range(15):
    for j in range(5):
        if(len(list1[j][0])<=i):
            pass       
        else:
            print(list1[j][0][i],end='')
    