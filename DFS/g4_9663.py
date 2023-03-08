import sys
sys.setrecursionlimit(10**9)


def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for d in range(N):
        if not (visited1[d] or visited2[n+d] or visited3[n-d]):
            visited1[d] = visited2[n+d] = visited3[n-d] = 1
            dfs(n+1)
            visited1[d] = visited2[n+d] = visited3[n-d] = 0


N = int(input())

visited1 = [0]*N
visited2 = [0]*(2*N)
visited3 = [0]*(2*N)

cnt = 0
dfs(0)

print(cnt)
