import sys
input = sys.stdin.readline

K = int(input())
max_height = 0
max_width = 0
arr = []
for i in range(6):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if temp[0] == 1 or temp[0] == 2:  
        if max_width < temp[1]:
            max_width = temp[1]
    else:
        if max_height < temp[1]:
            max_height = temp[1]

minus = 0
for i in range(6):
    if arr[i][0] == arr[(i+2) % 6][0] and arr[(i+1) % 6][0] == arr[(i+3) % 6][0]:
        minus = arr[(i+1) % 6][1]*arr[(i+2) % 6][1]
        break

print((max_height*max_width-minus)*K)



