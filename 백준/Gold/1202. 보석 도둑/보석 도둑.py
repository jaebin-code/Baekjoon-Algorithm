import sys

import heapq

input=sys.stdin.readline
N,K = map(int,sys.stdin.readline().split())
gem = []
for _ in range(N):
    M,V = map(int,sys.stdin.readline().split())
    heapq.heappush(gem, [M, V])
bag = []
for _ in range(K):
    C = int(sys.stdin.readline().strip())
    heapq.heappush(bag, C)
heaplist=[]
result=0
for _ in range(K):
    bagitem=heapq.heappop(bag)

    while gem and bagitem>=gem[0][0]:
        [a,b]=heapq.heappop(gem)
        heapq.heappush(heaplist,-b)
    if heaplist:
        result-=heapq.heappop(heaplist)
    elif not gem:
        break
print(result)