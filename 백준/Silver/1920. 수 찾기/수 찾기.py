def binarysearch(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        ans=arr[mid]
        if(ans==target):
            return 1
        elif ans>target:
            end=mid-1
        else:
            start=mid+1
    return 0

n=int(input().rstrip())
list1=list(map(int,input().split()))
list1.sort()

m=int(input().rstrip())
list2=list(map(int,input().split()))
for i in range(m):
    print(binarysearch(list1,list2[i]))