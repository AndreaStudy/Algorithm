import sys
input = sys.stdin.readline
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()
visited[0][0] = 1
q.append((0,0))
while q:
    x, y = q.popleft()
    if x == M-1 and y == N-1:
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or M <= nx or 0 > ny or N <= ny:
            continue
        if arr[ny][nx] == '1' and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append((nx, ny))

print(visited[N-1][M-1])