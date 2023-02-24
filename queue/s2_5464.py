import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
cost = [int(input()) for _ in range(N)]
cars = [int(input()) for _ in range(M)]
seq = [int(input()) for _ in range(2*M)]
visited = [0] * N
result = 0
q = deque()
for i in seq:
    if 0 in visited:
        if i > 0:
            for j in range(N):
                if visited[j] == 0:
                    result += (cost[j]*cars[i-1])
                    visited[j] = i
                    break
        else:
            i = abs(i)
            for j in range(N):
                if visited[j] == i:
                    visited[j] = 0
                    if q:
                        temp = q.popleft()
                        result += (cost[j]*cars[temp-1])
                        visited[j] = temp
                        print('wow')
                    break
                
    else:
        print(i, *visited)
        print(1111)
        q.append(i)

print(result)



