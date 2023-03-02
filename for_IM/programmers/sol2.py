from collections import deque
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution(board):
    n = len(board)

    visit = deque()
    visit.append([0, 0])

    # 0은 세로 1은 가로
    visited = [[[INF for _ in range(n)] for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = 0
    visited[1][0][0] = 0

    while visit:
        x, y = visit.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                continue

            # 가로 진입시
            if dir % 2:
                temp = min(visited[1][x][y] + 1, visited[0][x][y] + 6)
                if visited[1][nx][ny] > temp:
                    visited[1][nx][ny] = temp
                    visit.append([nx, ny])
            
            # 세로 진입시
            else:
                temp = min(visited[1][x][y] + 6, visited[0][x][y] + 1)
                if visited[0][nx][ny] > temp:
                    visited[0][nx][ny] = temp
                    visit.append([nx, ny])

    for i in visited[0]:
        print(*i)

    for i in visited[1]:
        print(*i)

    return min(visited[0][n-1][n-1], visited[1][n-1][n-1]) * 100

input_data = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(input_data))
