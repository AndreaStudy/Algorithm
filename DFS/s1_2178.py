import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt, result
    if cnt >= result:
        return
    if x == M-1 and y == N-1:
        if result > cnt:
            result = cnt
        return
    if cnt == N+M-1:
        return
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and arr[ny][nx] == 1:
            visited[ny][nx] = 1
            cnt += 1
            dfs(nx, ny)
            visited[ny][nx] = 0
            cnt -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 1
result = N*M
dfs(0,0)
print(result)