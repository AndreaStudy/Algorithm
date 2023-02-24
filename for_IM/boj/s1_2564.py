import sys
input = sys.stdin.readline

x, y = map(int, input().split())
N = int(input())
store = [list(map(int, input().split())) for _ in range(N)]
dongeun = list(map(int, input().split()))

result = 0
# 남쪽이나 북쪽
for i in range(N):
    if dongeun[0] == 1:
        if store[i][0] == 1:
            result += abs(store[i][1]-dongeun[1])
        elif store[i][0] == 2:
            result += min(dongeun[1]+store[i][1]+y, (2*x-dongeun[1]-store[i][1])+y)
        elif store[i][0] == 3:
            result += (dongeun[1]+store[i][1])
        else:
            result += ((x-dongeun[1])+store[i][1])
    elif dongeun[0] == 2:
        if store[i][0] == 1:
            result += min(dongeun[1]+store[i][1]+y, (2*x-dongeun[1]-store[i][1])+y)
        elif store[i][0] == 2:
            result += abs(store[i][1]-dongeun[1])
        elif store[i][0] == 3:
            result += (dongeun[1]+(y-store[i][1]))
        else:
            result += ((x-dongeun[1])+(y-store[i][1]))
    elif dongeun[0] == 3:
        if store[i][0] == 1:
            result += (dongeun[1]+store[i][1])
        elif store[i][0] == 2:
            result += ((y-dongeun[1])+store[i][1])
        elif store[i][0] == 3:
            result += abs(store[i][1]-dongeun[1])
        else:
            result += min(dongeun[1]+store[i][1]+x, (2*y-dongeun[1]-store[i][1])+x)
    else:
        if store[i][0] == 1:
            result += (dongeun[1]+(x-store[i][1]))
        elif store[i][0] == 2:
            result += ((y-dongeun[1])+(x-store[i][1]))
        elif store[i][0] == 3:
            result += min(dongeun[1]+store[i][1]+x, (2*y-dongeun[1]-store[i][1])+x)
        else:
            result += abs(store[i][1]-dongeun[1])

print(result)