from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    
    while prices:
        temp = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if(temp > i):
                break
        answer.append(cnt)
    return answer