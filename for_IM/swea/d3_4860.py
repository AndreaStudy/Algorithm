T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = 'Possible'
    arr.sort()
    for t in arr:
        cnt += 1
        if cnt > (t//M)*K:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')