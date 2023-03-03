import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1]

N, K = map(int, input().split())

if N < K:
    visited = [[0, 0] for _ in range(100001)]
    visited[N][0] = 1
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            break
        for d in range(3):
            if d == 2:
                nx = x*2
            else:
                nx = x +dx[d]
            if 0 > nx or nx > 100000:
                continue
            if visited[nx] == [0,0]:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] = x
                q.append(nx)
    print(visited[K][0]-1)
    result = [K]
    temp = visited[K][1]
    while temp != N:
        result.append(temp)
        temp = visited[temp][1]
    result.append(N)
    result.reverse()
    print(*result)
    
elif N > K:
    print(N-K)
    result = list(range(N, K-1, -1))
    print(*result)
else:
    print(0)
    print(N)
