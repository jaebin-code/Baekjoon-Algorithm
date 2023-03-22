number = list(map(int,input().split()))
answer=[1,1,2,2,2,8]
for i in range(len(answer)):
    print(answer[i]-number[i],end=" ")