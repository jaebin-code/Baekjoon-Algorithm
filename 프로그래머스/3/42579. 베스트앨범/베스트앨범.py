def solution(genres, plays):
    firstDic = {}
    secondDic = {}
    answer = []
    
    for i in range(0,len(genres)):
        if genres[i] not in firstDic:
            firstDic[genres[i]] = [[i,genres[i],plays[i]]]
        else:
            firstDic[genres[i]].append([i,genres[i],plays[i]])
            
        if genres[i] not in secondDic:
            secondDic[genres[i]] = plays[i]
        else:
            secondDic[genres[i]] += plays[i]
            
    secondDic = sorted(secondDic.items(), key=lambda x:x[1], reverse=True)
    for i in secondDic:
        if len(firstDic[i[0]]) == 1:
            answer.append(firstDic[i[0]][0][0])
        else:
            answer.append(sorted(firstDic[i[0]], key=lambda x:x[2], reverse=True)[:2][0][0])
            answer.append(sorted(firstDic[i[0]], key=lambda x:x[2], reverse=True)[:2][1][0])
    return answer