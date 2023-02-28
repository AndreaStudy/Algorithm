T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N >= M:
        A, B = B, A
        N, M = M, N
    result = []
    for i in range(M-N+1):
        s_result = 0
        for j in range(N):
            s_result += (A[j]*B[i+j])
        result.append(s_result)

    print(f'#{tc} {max(result)}')