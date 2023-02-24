import sys
input = sys.stdin.readline

N = int(input())
answer = [0, 0, 0]
li = [list(map(int, input().split())) for _ in range(N)]

def checker(start, end, size):
    color = li[start][end]
    if size > 1:
        for y in range(start, start + size):
            for x in range(end, end + size):
                if li[y][x] != color:
                    n_size = size//3
                    for i in range(3):
                        for j in range(3):
                            checker(start + i * n_size, end + j * n_size, n_size)
                    return
    answer[color + 1] += 1
checker(0, 0, N)
print('\n'.join(map(str, answer)))