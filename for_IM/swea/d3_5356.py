T = int(input())

for tc in range(1, T+1):
    arr = [input() for  _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            try:
                ans += arr[i][j]
            except:
                pass
    print(f'#{tc} {ans}')