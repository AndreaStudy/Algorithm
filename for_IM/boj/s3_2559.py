import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))
if N > 2:
    result = []
    total = 0
    for i in range(N):
        total += temp[i]
        result.append(total)

    ans = result[K-1]
    for i in range(K, N):
        if ans < (result[i]-result[i-K]):
            ans = (result[i]-result[i-K])
else:
    if K == 2:
        ans = sum(temp)
    else:
        ans = max(temp)

print(ans)