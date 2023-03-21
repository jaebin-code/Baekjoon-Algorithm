list1=[0 for i in range(30)]
for i in range(28):
    list1[int(input())-1]=1
for j in range(30):
    if(list1[j]==0):
        print(j+1)