T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    cnt = []
    for row in arr:
        W = row.count('W')
        B = row.count('B')
        R = M - W - B 
        cnt.append([W, B, R])
    for i in range(1, N):
        cnt[i][0] += cnt[i-1][0]
        cnt[i][1] += cnt[i-1][1]
        cnt[i][2] += cnt[i-1][2]

    max_cnt = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            white = cnt[i][0]
            blue = cnt[j][1] - cnt[i][1]
            red = cnt[N-1][2] - cnt[j][2]
            max_cnt.append(white+blue+red)

    print(f'#{tc} {N*M-max(max_cnt)}')