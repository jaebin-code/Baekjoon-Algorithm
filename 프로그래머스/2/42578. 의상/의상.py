def solution(clothes):
    answer = 1
    clothesDic = {}
    
    for i in clothes:
        if i[1] in clothesDic:
            clothesDic[i[1]] += 1
        else:
            clothesDic[i[1]] = 1
    for i in clothesDic.values():
        answer *= i+1;
    
    return answer-1