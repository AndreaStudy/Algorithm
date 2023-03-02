T = int(input())

dx = [1, 0]
dy = [0, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[[0,0] for _ in range(N)] for _ in range(N)]
    result = []
    stack = []

    for j in range(N):
        for i in range(N):
            if arr[j][i] != 0:
                arr[j][i] = 0
                visited[j][i][0] = 1
                visited[j][i][1] = 1
                stack.append((i,j))
                while stack:
                    x, y = stack.pop(0)
                    for d in range(2):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[ny][nx] != 0:
                                arr[ny][nx] = 0
                                stack.append((nx, ny))
                                if d == 0:
                                    visited[ny][nx][1] = visited[y][x][1] + 1
                                    visited[ny][nx][0] = visited[y][x][0]
                                else:
                                    visited[ny][nx][1] = visited[y][x][1]
                                    visited[ny][nx][0] = visited[y][x][0] + 1
                    if not stack:
                        result.append(visited[y][x])

    result.sort(key = lambda x:x[0])
    result.sort(key = lambda x:x[0]*x[1])

    print(f'#{tc} {len(result)}', end=" ")
    for i in result:
        print(*i, end=" ")
    print()
