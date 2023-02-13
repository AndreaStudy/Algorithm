import sys
input = sys.stdin.readline

# 반복횟수 K입력
K = int(input())
# 스택을 생성
stack = []

# K만큼 반복
for _ in range(K):
    # num 값 입력
    num = int(input())
    # 0이 아니라면
    if num != 0:
        # 스택에 값을 넣어줌
        stack.append(num)
    # 0일경우 stack에서 값을 꺼내줌
    else:
        stack.pop()
# 결과값을 저장할 변수
result = 0
# 스택에 값이 있다면
if stack:
    # 스택을 순회하면 안에 있는 값들을 더해줌
    for i in stack:
        result += i

print(result)