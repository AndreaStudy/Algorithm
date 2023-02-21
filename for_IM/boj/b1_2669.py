import sys
input = sys.stdin.readline

arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    a,b,c,d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1
    
result = 0
for row in arr:
    result += row.count(1)

print(result)
