import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
max_arr = 0
stack = []
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if max(temp) > max_arr:
        max_arr = max(temp)

ans = 0
for K in range(max_arr):
    result = 0
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            cnt = 0
            if arr[j][i] > K and visited[j][i] == 0:
                visited[j][i] = 1
                cnt += 1
                stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 and arr[y][x] > K:
                        visited[ny][nx] = 1
                        stack.append((nx, ny))
            if cnt > 0:
                result += 1
    ans = max(ans, result)

print(ans)
