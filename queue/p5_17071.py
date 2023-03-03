# 포기


import sys
input = sys.stdin.readline
from collections import deque

def find():
    global K
    visited = [[0, 0] for _ in range(500001)]
    q = deque()
    q.append(N)
    visited[N][0] = 1
    visited[N][1] = 0
    temp = 0
    while q:
        x = q.popleft()
        temp =  K+visited[x][1]
        print(x, temp, visited[x])
        if temp > 500000:
            return -1
        if x == temp:
            break
        for d in range(3):
            if d == 2:
                nx = x*2
            else:
                nx = x +dx[d]
            if 0 > nx or nx > 500000:
                continue
            visited[nx][0] = visited[x][0] + 1
            visited[nx][1] = visited[x][0] + visited[x][1]
            q.append(nx)
    return visited[temp][0]-1


dx = [-1, 1]

N, K = map(int, input().split())

if N == K:
    print(0)
else:
    print(find())
