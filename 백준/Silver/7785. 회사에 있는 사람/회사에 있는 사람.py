import sys
namelist=[]
a=int(sys.stdin.readline())
for _ in range(a):
    name,status=map(str,sys.stdin.readline().split())
    if(status=="enter"):
        namelist.append(name)
    else:
        namelist.remove(name)
namelist.sort(reverse=True)
for i in range(len(namelist)):
    print(namelist[i])