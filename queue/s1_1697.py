import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1]

N, K = map(int, input().split())

if N < K:
    visited = [0]*(100001)
    q = deque()
    q.append(N)
    visited[N] = 1
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
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
    print(visited[K]-1)
elif N > K:
    print(N-K)
else:
    print(0)
