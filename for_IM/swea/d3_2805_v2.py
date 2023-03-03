T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    k = N//2
    result = 0
    for i in range(N):
        for j in range(abs(k-i), N-abs(k-i)):
            result += arr[i][j]

    print(f'#{tc} {result}')