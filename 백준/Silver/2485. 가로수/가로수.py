length=int(input())
li=[]
for _ in range(length):
    li.append(int(input()))
li.sort()
li2=[]
for i in range(len(li)-1):
    li2.append(li[i+1]-li[i])
gcd=0
for i in range(len(li2)):
    a,b=min(li2[i],gcd),max(li2[i],gcd)
    x,y=a,b
    while x!=0:
        x,y=y%x,x
    gcd=y
print(((max(li)-min(li))//gcd)-1-(len(li)-2))
    