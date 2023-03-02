def findarr(x, y):
    r, c = 0, 0
    while arr[x+r][y]: r += 1
    while arr[x][y+c]: c += 1
 
    for i in range(r):
        for j in range(c):
            arr[x+i][y+j] = 0
    return (r, c)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    result = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                result.append(findarr(i, j))
                cnt += 1
 
    result.sort(key=lambda x: (x[0]*x[1], x[0]))

    print(f'#{tc} {cnt}', end=" ")
    for i in result:
        print(*i, end=" ")
    print()