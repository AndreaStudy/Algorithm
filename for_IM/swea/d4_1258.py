T = int(input())

dx = [1, 0]
dy = [0, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[[0,0]]*N for _ in range(N)]
    result = []
    stack = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0:
                arr[y][x] = 0
                visited[y][x][0] = 1
                visited[y][x][1] = 1
                stack.append((x,y))
                while stack:
                    x, y = stack.pop(0)
                    for d in range(2):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[ny][nx] != 0 and visited[ny][nx] == [0,0]:
                                arr[ny][nx] = 0
                                stack.append((nx, ny))
                                if d == 0:
                                    visited[ny][nx][1] = visited[y][x][1] + 1
                                else:
                                    visited[ny][nx][0] = visited[y][x][0] + 1
                    if not stack:
                        result.append(visited[y][x])

    for i in visited:
        print(*i)
