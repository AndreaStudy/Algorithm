board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

INF = int(10e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    length = len(board)
    stack = [(0,0)]
    visited = [[[INF for _ in range(2)]  for _ in range(length)] for _ in range(length)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0

    while stack:
        x, y = stack.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < length and 0 <= ny < length:
                if board[ny][nx] == 0:
                    if d in [0,2]:
                        temp = min(visited[y][x][1]+1, visited[y][x][0]+6)
                        if visited[ny][nx][1] > temp:
                            visited[ny][nx][1] = temp
                            stack.append((nx, ny))
                    else:
                        temp = min(visited[y][x][1]+6, visited[y][x][0]+1)
                        if visited[ny][nx][0] > temp:
                            visited[ny][nx][0] = temp
                            stack.append((nx, ny))

    return min(visited[length-1][length-1][0], visited[length-1][length-1][1]) * 100

print(solution(board))
