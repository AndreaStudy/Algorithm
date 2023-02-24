import sys
input = sys.stdin.readline

N = int(input())

arr = [input().split() for _ in range(N)]
a1, a2, a3 = 0, 0, 0
stack = []
stack.append((arr, N))
while stack:
    arr, N = stack.pop()
    
    if N == 1:
        if arr[0][0] == '0':
            a1 += 1
            continue
        elif arr[0][0] == '1':
            a2 += 1
            continue
        else:
            a3 += 1
            continue

    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in arr:
        cnt_0 += i.count('0')
        cnt_1 += i.count('1')
        cnt_2 += i.count('-1')

    if cnt_0 == N*N:
        a1 += 1
        continue
    elif cnt_1 == N*N:
        a2 += 1
        continue
    elif cnt_2 == N*N:
        a3 += 1
        continue
    
    k = N//3

    for i in range(0, N, k):
        for j in range(0, N, k):
            new_arr = [[0]*k for _ in range(k)]
            for a in range(k):
                for b in range(k):
                    new_arr[a][b] = arr[i+a][j+b]
            stack.append((new_arr, k))

print(a3)
print(a1)
print(a2)