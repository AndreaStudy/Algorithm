import sys
input = sys.stdin.readline

def solution(idx, people):
    global result

    if people == N // 2:
        start = 0
        link = 0
        # 반복문을 통해 팀 능력치 조사
        for i in range(N):
            for j in range(N):
                # 스타트 팀 능력치
                if visited[i] and visited[j]:
                    start += arr[i][j]

                # 링크 팀 능력치
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]

        # 스타트 팀의 능력치와 링크 팀의 능력치의 최소 값을 구한다.
        result = min(result, abs(start - link))
        return

    # 반복문과 백트래킹을 통해 통해 팀을 구성할 수 있는 경우의 수 확인
    for x in range(idx, N):
        if not visited[x]:
            visited[x] = 1
            solution(x + 1, people + 1)
            visited[x] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = int(10e9)
solution(0, 0)
print(result)