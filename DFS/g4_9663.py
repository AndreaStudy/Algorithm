import sys
sys.setrecursionlimit(10**9)

dx = [-1, 0, 1]
dy = [-1, -1, -1]

def check(a, b):
    for d in range(3):
        i = 1
        while True:
            ny = a + i*dy[d]
            nx = b + i*dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1:
                    return False
            else:
                break
            i += 1
    return True


def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for d in range(N):
        if visited[d] == 0:
            visited[d] = 1
            arr[n][d] = 1
            if check(n, d):
                dfs(n+1)
            visited[d] = 0
            arr[n][d] = 0

N = int(input())

visited = [0]*N
arr = [[0]*N for _ in range(N)]
cnt = 0
dfs(0)

print(cnt)

