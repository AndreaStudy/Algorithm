T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    
    result = -1
    for i in range(N - 1):
        for j in range(i+1, N):
            num = A[i] * A[j]
            if result > num:
                break
            temp = num
            next = temp % 10
            temp //= 10
            while temp:
                prev = temp % 10
                if prev > next:
                    break
                next = prev
                temp //= 10
            else:
                result = num
    print(f'#{tc} {result}')

