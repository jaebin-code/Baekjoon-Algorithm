def solution(arr):
    answer = []
    idx = 0
    if len(arr) == 0:
        return answer
    answer.append(arr[0])
    
    for i in range(len(arr)-1):
        if(answer[idx] != arr[i+1]):
            answer.append(arr[i+1])
            idx += 1
    return answer