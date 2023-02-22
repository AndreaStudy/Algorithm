import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]

s = []
for _ in range(5):
    s += list(map(int, input().split()))

cnt = 0
result = 0
for n in s:
    check = True
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0
                cnt += 1
                check = False
                break
        if not check:
            break
    if cnt >= 12:
        x1_cnt = 0
        x2_cnt = 0
        for i in range(5):
            row_cnt = 0
            col_cnt = 0
            for j in range(5):
                if arr[i][j] == 0:
                    row_cnt += 1
                if arr[j][i] == 0:
                    col_cnt += 1
            if i == 0:
                if arr[i][i] == 0:
                    x1_cnt += 1
                if arr[i][-i-1] == 0:
                    x2_cnt += 1
            if row_cnt == 5:
                result += 1
                print('row')
            if col_cnt == 5:
                result += 1
                print('col')
        if x1_cnt == 5:
            result += 1
            print('x1')
        if x2_cnt == 5:
            result += 1
            print('x2')
        if result >= 3:
            for k in arr:
                print(*k)
            print(cnt)
            exit()