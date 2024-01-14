def solution(progresses, speeds):
    day = 0
    answer = []
    cnt = 0
    while(len(progresses) != 0):
        if(progresses[0] + speeds[0] * day >= 100):
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            for i in range(len(progresses)):
                if(progresses[0] + speeds[0] * day < 100):
                    break
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
        if(cnt != 0):
            answer.append(cnt)
            cnt = 0
        day += 1
    return answer