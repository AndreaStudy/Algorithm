import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    if len(command) == 2:
        stack.append(command[-1])
    else:
        if command[0] == 'top':
            print(stack[-1])
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif command[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
