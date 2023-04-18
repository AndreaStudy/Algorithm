import sys
input = sys.stdin.readline
from collections import deque  

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N, M = map(int,input().split())
maze = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0] = 1
    while q:
        x,y,broken = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if maze[nx][ny] == '0':
                    q.append((nx,ny,broken))
                    visited[nx][ny] = visited[x][y] + 1
                if broken == 0 and maze[nx][ny] == '1':
                    q.append((nx,ny,1))
                    visited[nx][ny] = visited[x][y] + 1
    return -1
print(bfs())
for i in visited:
    print(*i)


            