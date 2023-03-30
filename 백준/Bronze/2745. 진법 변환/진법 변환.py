n,k=input().split()
k=int(k)
liststr=list(n)
liststr.reverse()
cnt=0
result=0
for i in range(len(liststr)):
    if (ord(liststr[i])<=90 and ord(liststr[i])>=65):
        result+=(ord(liststr[i])-55)*(k**cnt)
    else:
        result+=(int(liststr[i]))*(k**cnt)
    cnt+=1
print(result)