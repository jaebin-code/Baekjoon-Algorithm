list1=[]
for i in range(5):
    list1.append(int(input()))
list1.sort()
print(int(sum(list1)/5))
print(list1[2])
