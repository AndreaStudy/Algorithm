import sys
input = sys.stdin.readline

cnt = 0
result = []

def DFS(x, y):
    global cnt
    arr[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny] == 1:
            DFS(nx, ny)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i, j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
