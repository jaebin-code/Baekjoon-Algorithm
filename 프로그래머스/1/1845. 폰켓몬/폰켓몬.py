def solution(nums):
    numsLen = len(nums)/2
    numsList = []
    answer = 0
    
    for i in nums:
        if i in numsList:
            continue
        else:
            numsList.append(i)
    if (len(numsList) >= numsLen):
        return numsLen
    else:
        return len(numsList)