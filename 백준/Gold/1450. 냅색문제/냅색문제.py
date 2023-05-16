import sys
from itertools import combinations
input=sys.stdin.readline

def binarysearch(arr,target,start,end):
    while start<end:
        mid=(start+end)//2
        if(arr[mid]<=target):
            start=mid+1
        else:
            end=mid
    return end

n,c=map(int,input().split())
len1=n//2
len2=n//2+1
arr=list(map(int,input().split()))
arr1=arr[0:len1]
arr2=arr[len2-1:n]
comb1=[]
comb2=[]
cnt=0
for i in range(0,len1+1):
    for j in combinations(arr1,i):
        comb1.append(sum(j))
for i in range(0,n-len2+2):
    for j in combinations(arr2,i):
        comb2.append(sum(j))
comb2.sort()
for i in comb1:
    if c-i<0:
        continue
    cnt+=binarysearch(comb2,c-i,0,len(comb2))
print(cnt)