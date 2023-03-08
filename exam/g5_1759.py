import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(cnt, idx):

    if cnt == L:
        moeum, jaeum = 0, 0

        for i in range(L):
            if answer[i] in 'aeiou':
                moeum += 1
            else:
                jaeum += 1

        if moeum >= 1 and jaeum >= 2:
            print("".join(answer))

        return

    for i in range(idx, C):
        answer.append(arr[i])
        dfs(cnt + 1, i + 1)
        answer.pop()


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

answer = []
dfs(0, 0)
