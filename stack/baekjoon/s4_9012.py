import sys
input = sys.stdin.readline

# 함수
def test(sik):
    # 스택을 생성
    stack = []
    # 기본 리턴 값 'YES'
    word = 'YES'
    # 입력받은 값을 순회하면 체크
    for i in sik:
        # '(' 라면 스택에 push
        if i == '(':
            stack.append(i)
        # 아니라면 
        else:
            # 스택에 값이 존재할 경우 pop
            if stack:
                stack.pop()
            # 값이 없다면 NO 를 리턴
            else:
                word = 'NO'
                return word
    # 반복문이 모두 끝난뒤
    # 스택에 값이 있다면 NO를 리턴
    if stack:
        word = 'NO'
        return word
    # 값이 없다면 YES를 리턴
    else:
        return word

# 테스트 케이스 입력
T = int(input())

# 식을 입력받고 함수호출
for _ in range(T):
    sik = input().rstrip()
    print(test(sik))
