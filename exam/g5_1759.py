import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n, cnt, check):
    global result
    if cnt == 4 and check:
        print(result)
        return
    for i in range(n, C):
        if visited[i] == 0:
            temp = result
            result = result + arr[i]
            visited[i] = 1
            if arr[i] in idx:
                dfs(i, cnt+1, True)
            else:
                dfs(i, cnt+1, check)
            result = temp
            visited[i] = 0


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
idx = []
visited = [0] * C
for i in range(C):
    if arr[i] in 'aeiou':
        idx.append(arr[i])

result = ''
dfs(0, 0, False)
