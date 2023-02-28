T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        print(N//i, end=' ')
        N %= i
    print()
