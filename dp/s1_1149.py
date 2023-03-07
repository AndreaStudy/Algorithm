import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(n, m):
    global result, total
    if n != 0:
        visited[m] = 1
    if n == N:
        print(result, total)
        if result > total:
            result = total
        return
    for i in range(3):
        if visited[i] == 0:
            total += arr[n][i]
            find(n+1, i)
            total -= arr[n][i]
        else:
            continue

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*3

result = 1000*N
total = 0

find(0, 0)
print(result)