listlen=int(input())
if (listlen<2):
    for i in range(listlen):
        a,b=map(int,input().split())
    print(0)
else:
    a,b=map(int,input().split())
    listx1=a
    listx2=a
    listy1=b
    listy2=b
    for i in range(listlen-1):
        a,b=map(int,input().split())
        listx1=min(a,listx1)
        listx2=max(a,listx2)
        listy1=min(b,listy1)
        listy2=max(b,listy2)
    print((listx2-listx1)*(listy2-listy1))