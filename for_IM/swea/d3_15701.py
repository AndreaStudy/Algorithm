
for tc in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    ans = 0
    for st in zip(*arr):
        ans += "".join(st).replace('0', '').count('12')

    print(f'#{tc} {ans}')