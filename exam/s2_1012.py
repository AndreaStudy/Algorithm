import sys
input = sys.stdin.readline

# 오 아 왼 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    stack = []
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        visited[y][x] = 1
    result = 0

    for y in range(N):
        for x in range(M):
            if visited[y][x] == 1:
                visited[y][x] = 0
                stack.append((x, y))
                cnt = 0
                while stack:
                    sx, sy = stack.pop()
                    for d in range(4):
                        nx = sx + dx[d]
                        ny = sy + dy[d]
                        if 0 <= nx < M and 0 <= ny < N:
                            if visited[ny][nx] == 1:
                                visited[ny][nx] = 0
                                cnt += 1
                                stack.append((nx, ny))
                if cnt > 0:
                    result += 1
                    cnt = 0

    print(result)
