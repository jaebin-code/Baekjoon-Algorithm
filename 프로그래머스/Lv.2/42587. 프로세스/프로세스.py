def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    cnt = 0
    while(len(queue) != 0):
        cur = queue.pop(0)
        if(any(cur[1] < q[1] for q in queue)):
            queue.append(cur)
        else:
            if(cur[0] == location):
                return cnt + 1
            cnt += 1