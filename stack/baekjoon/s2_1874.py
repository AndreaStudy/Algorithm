import sys
input = sys.stdin.readline

n = int(input())

# 숫자를 세어줄 변수
count = 1
stack = []
result = []

# 반복
for i in range(1, n + 1):
    # 입력값
    data = int(input())
    # 입력값만큼 stack에 push
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    # stack에 마지막에 들어간 값이랑 같으면 가능
    # 마지막에 들어간 값과 다르면 불가능
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
# result에 저장한 값들과 띄워쓰기로 join에서 출력
print('\n'.join(result))