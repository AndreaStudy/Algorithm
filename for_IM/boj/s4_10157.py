import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

C, R = map(int, input().split())
visited = [[0]*C for _ in range(R)]
target = int(input())
stack = [(0,0)]
num = 1
d = 0
if target > C*R:
    print(0)
else:
    while stack:
        x, y = stack.pop()
        visited[y][x] = num
        num += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < C and 0 <= ny < R and visited[ny][nx] == 0:
            stack.append((nx, ny))
        else:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < C and 0 <= ny < R:
                if visited[ny][nx] == 0:
                    stack.append((nx, ny))

    for i in visited:
        try:
            print(i.index(target)+1, visited.index(i)+1)
        except:
            pass


