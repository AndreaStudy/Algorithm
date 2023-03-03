import sys
input = sys.stdin.readline
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
q = deque()
visited = [[0]*N for _ in range(M)]

no = 0
cnt = 0
for y in range(M):
    for x in range(N):
        if arr[y][x] == 1:
            q.append((x,y))
            visited[y][x] = 1
            cnt += 1
        elif arr[y][x] == -1:
            no += 1

while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny <0 or ny >= M:
            continue
        if arr[ny][nx] == 0:
            arr[ny][nx] = 1
            visited[ny][nx] = visited[y][x] + 1
            cnt += 1
            q.append((nx, ny))


result = -1
if cnt != (M*N-no):
    print(result)
else:
    for i in visited:
        if result < max(i):
            result = max(i)
    print(result-1)