import sys
input = sys.stdin.readline

# 괄호가 맞는지 여부를 확인할 함수
def test(word):
    # 스택을 생성
    stack = []
    # 기본 result 값은 no
    result = 'no'
    # 입력받은 글자를 순회하면서 체크
    for i in word:
        # '(', '[' 일경우 stack에 추가
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        # ')' 일 경우
        elif i == ')':
            # 스택에 값이 있다면
            if stack:
                # 그 값을 꺼내서 괄호가 쌍을 이루는지 확인
                # 쌍을 이루지 않는다면 no를 리턴
                if stack.pop() != '(':
                    return result
            # 스택에 값이 없다면 마찬가지로 no로 리턴
            else:
                return result
        # ']' 일 경우
        elif i == ']':
            # 스택에 값이 존재한다면
            if stack:
                # 그 값을 꺼내서 대괄호가 쌍을 이루는지 확인
                # 쌍을 이루지 않는다면 no를 리턴
                if stack.pop() != '[':
                    return result
            # 스택에 값이 없다면 마찬가지로 no를 리턴
            else:
                return result
    # 반복문이 모두 끝나고 난뒤
    # 안에 괄호가 존재한다면 쌍을 이루지 않기 떄문에 no를 리턴
    if stack:
        return result
    # 모든 체크가 끝나고 난뒤에는 yes를 리턴
    result = 'yes'
    return result

# 종료조건이 입력될때까지 반복해서 진행
while True:
    # 입력
    word = input().rstrip()
    # 종료조건 '.'만이 입력되을 경우
    if word == '.':
        break
    # 함수호출해서 리턴값 출력
    print(test(word))