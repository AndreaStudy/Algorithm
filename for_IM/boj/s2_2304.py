import sys
input = sys.stdin.readline


N = int(input())
bar = [list(map(int, input().split())) for _ in range(N)]

bar.sort(key=lambda x:x[0])
result = 0

x,y = bar[0][0], bar[0][1]
for i in range(1, N):
    nx, ny = bar[i][0], bar[i][1]
    if ny >= y:
        result += ((nx-x)*y)
        y = ny
        x = nx
result += y
bar.reverse()
x, y = bar[0][0], bar[0][1]
for i in range(1, N):
    nx, ny = bar[i][0], bar[i][1]
    if ny > y:
        result += ((x-nx)*y)
        y = ny
        x = nx

print(result)
         

