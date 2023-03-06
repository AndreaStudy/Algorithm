T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minV = 1000
    
    size = [0] * 31 # 당근의 크기 1~30
    for c in arr:   # 크기별로 개수 파악
        size[c] += 1

    for i in range(29): # 소박스
        for j in range(i+1, 30): # 중 박스
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:31])
            if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                diff = max(A,B,C) - min(A,B,C)
                if minV > diff:
                    minV = diff
    
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')
