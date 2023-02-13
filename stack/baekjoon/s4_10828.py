import sys
input = sys.stdin.readline

# 반복 횟수 N입력
N = int(input())
# 스택 생성
stack = []
# N번 만큼 반복
for _ in range(N):
    # 명령어 입력
    command = input().split()
    # command의 길이가 1일경우
    if len(command) == 1:
        command = command[0]
        # command가 top일 경우
        if command == 'top':
            # 스택에 값이 있다면 마지막값을 보여주고
            if stack:
                print(stack[-1])
            # 스택에 값이 없다면 -1을 출력
            else:
                print(-1)
        # command가 size일 경우
        elif command == 'size':
            # stack의 길이를 출력
            print(len(stack))
        # command가 empty일 경우
        elif command == 'empty':
            # 안에 값이 있다면 0 없다면 1을 출력
            if stack:
                print(0)
            else:
                print(1)
        # command가 pop일 경우
        elif command == 'pop':
            # stack에 값이 있다면 스택에 값을 꺼내서 출력
            if stack:
                print(stack.pop())
            # stack에 값이 없다면 -1출력
            else:
                print(-1)
    # push일경우 입력 값과 함께 들어오기 때문에 입력값의 길이가 1이아님
    else:
        stack.append(command[-1])
        
