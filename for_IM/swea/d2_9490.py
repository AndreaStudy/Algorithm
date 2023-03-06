T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = 0
    max_V = 0

    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            for k in range(1, arr[i][j]+1):
                if i+k < N:
                    temp += arr[i+k][j]
                if j+k < M:
                    temp += arr[i][j+k]
                if i-k >= 0:
                    temp += arr[i-k][j]
                if j-k >= 0:
                    temp += arr[i][j-k]
            if max_V < temp:
                max_V = temp

    print(f'#{tc} {max_V}')
    

