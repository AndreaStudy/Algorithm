T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    k = N//2
    result = 0
    for i in range(N):
        for j in range(N):
            if abs(i-k) + abs(j-k) <= k:
                result += int(arr[i][j])

    print(f'#{tc} {result}')