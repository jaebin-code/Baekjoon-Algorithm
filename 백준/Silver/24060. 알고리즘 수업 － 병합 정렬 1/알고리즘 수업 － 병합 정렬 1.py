import sys
input=sys.stdin.readline
n,k=map(int,input().split())

def dividearr(arr):
    if len(arr)<=1:
        return arr
    mid=(len(arr)+1)//2
    left=arr[:mid]
    right=arr[mid:]
    left=dividearr(left)
    right=dividearr(right)
    return mergearr(left,right)
answer=[]
def mergearr(left,right):
    global answer
    result=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            answer.append(left[i])
            i+=1
        else:
            result.append(right[j])
            answer.append(right[j])
            j+=1
    while(i<len(left)):
        result.append(left[i])
        answer.append(left[i])
        i+=1
    while(j<len(right)):
        answer.append(right[j])
        result.append(right[j])
        j+=1
    return result
list1=list(map(int,input().split()))
dividearr(list1)
if(len(answer)>k):
    print(answer[k-1])
else:
    print(-1)