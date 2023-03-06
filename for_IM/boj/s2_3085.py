import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
arr_t = list(map(list,zip(*arr)))

for i in arr:
    print(*i)
for i in arr_t:
    print(*i)