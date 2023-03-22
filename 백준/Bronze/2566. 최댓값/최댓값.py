cnt=1
row=0
max=-1
idx=0
for i in range(9):
    list1=list(map(int,input().split()))
    for j in range(9):
        if(max<list1[j]):
            max=list1[j]
            row=cnt
            idx=j+1
    cnt+=1
print(max)
print(row,idx)