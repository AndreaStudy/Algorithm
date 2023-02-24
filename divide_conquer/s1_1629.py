import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a,b,c):
    # a의 b승은 a임
    if b==1:
        return a%c
    # a의 2승은 a*a
    elif b==2:
        return (a*a)%c
    # 그 외의 경우
    else:
        # b가 2의 배수면
        if b%2:
            return ((power(a,b//2,c)**2)*a)%c

        else:
            return ((power(a,b//2,c)**2))%c

print(power(A,B,C))