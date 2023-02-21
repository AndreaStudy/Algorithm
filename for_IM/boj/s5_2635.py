import sys
input = sys.stdin.readline

N = int(input())

target = N//2
r_cnt = 0
r_result = []
for i in range(target, N+1):
    result = [N, i]
    j = 0
    while True:
        diff = result[j] - result[j+1]
        if diff <= -1:
            break
        result.append(diff)
        if r_cnt < len(result):
            r_cnt = len(result)
            r_result = result
        j += 1

print(r_cnt)
print(*r_result)