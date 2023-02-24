import sys
input = sys.stdin.readline

T = int(input())

paper = [[0]* 1001 for _ in range(1001)]

if T == 1:
    x, y, w, h = map(int, input().split())
    print(w*h)
else:
    for i in range(1, T+1):
        x, y, w, h = map(int, input().split())
        for j in range(h):
            for k in range(w):
                paper[y+j][x+k] = i

    for i in range(1, T+1):
        result = 0
        for row in paper:
            result += row.count(i)
        print(result)