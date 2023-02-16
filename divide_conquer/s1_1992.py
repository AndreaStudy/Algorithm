import sys
input = sys.stdin.readline

def quard_tree(arr, N):
    global result
    white_cnt = 0
    black_cnt = 0
    for i in arr:
        white_cnt += i.count('0')
        black_cnt += i.count('1')
    if white_cnt == N*N:
        return '0'
    elif black_cnt == N*N:
        return  '1'
    k = N//2
    new_arr1 = [[0]*k for _ in range(k)]
    new_arr2 = [[0]*k for _ in range(k)]
    new_arr3 = [[0]*k for _ in range(k)]
    new_arr4 = [[0]*k for _ in range(k)]
    for i in range(0, k):
        for j in range(0, k):
            new_arr1[i][j] = arr[i][j]
            new_arr2[i][j] = arr[i][j+k]
            new_arr3[i][j] = arr[i+k][j]
            new_arr4[i][j] = arr[i+k][j+k]
    
    result = '(' + quard_tree(new_arr1, k) + quard_tree(new_arr2, k) + quard_tree(new_arr3, k) + quard_tree(new_arr4, k) + ')'

    return result

N = int(input())
arr = [input().rstrip() for _ in range(N)]
result = ''
print(quard_tree(arr, N))

