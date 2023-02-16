import sys
input = sys.stdin.readline

def make_paper(arr, N):
    global white, blue
    white_cnt = 0
    blue_cnt = 0
    for i in arr:
        white_cnt += i.count('0')
        blue_cnt += i.count('1')
    if white_cnt == N*N:
        white += 1
        return
    elif blue_cnt == N*N:
        blue += 1
        return
    k = N//2
    new_arr1 = [[0]*k for _ in range(k)]
    new_arr2 = [[0]*k for _ in range(k)]
    new_arr3 = [[0]*k for _ in range(k)]
    new_arr4 = [[0]*k for _ in range(k)]
    for i in range(0, k):
        for j in range(0, k):
            new_arr1[i][j] = arr[i][j]
            new_arr2[i][j] = arr[i+k][j]
            new_arr3[i][j] = arr[i][j+k]
            new_arr4[i][j] = arr[i+k][j+k]
    make_paper(new_arr1, k)
    make_paper(new_arr2, k)
    make_paper(new_arr3, k)
    make_paper(new_arr4, k)

N = int(input())
arr = [list(input().split()) for _ in range(N)]
white, blue = 0, 0
make_paper(arr, N)
print(white)
print(blue)
