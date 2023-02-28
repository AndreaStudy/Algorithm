T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    total = list(range(1, N+1))
    student = list(map(int, input().split()))

    result = []
    for i in total:
        if i not in student:
            result.append(i)

    print(f'#{tc}', *result)