stars=["***","* *","***"] #3인 경우
n=int(input())
cnt=0
while(n>3):
    n=n/3
    cnt=cnt+1

def makestars():
    newstars=[]
    L=len(stars)
    for i in range(L*3):
        if(i//L==1):
            newstars.append(stars[i%L]+" "*L+stars[i%L])
        else:
            newstars.append(stars[i%L]*3)
    return newstars
for i in range(cnt):
    stars=makestars()
for j in stars:
    print(j)