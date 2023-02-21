import sys
input = sys.stdin.readline

row, col = map(int, input().split())
N = int(input())
max_row = 0
max_col = 0
row_list = [0, row]
col_list = [0, col]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        col_list.append(b)
    else:
        row_list.append(b)

row_list.sort()
col_list.sort()

for i in range(len(row_list)-1):
    temp = row_list[i+1] - row_list[i]
    if max_row < temp:
        max_row = temp

for i in range(len(col_list)-1):
    temp = col_list[i+1] - col_list[i]
    if max_col < temp:
        max_col = temp

print(max_col*max_row)