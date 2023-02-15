import sys
input = sys.stdin.readline

# 시간초과
# N = int(input())
# numbers = list(map(int, input().split()))
# stack1 = []
# result = [-1]
# for i in numbers:
#     stack1.append(i)
# stack2 = [stack1.pop()]

# for i in range(len(stack1)):
#     temp = stack1.pop()
#     for j in stack2[::-1]:
#         if temp < j:
#             result.append(j)
#             break
#     else:
#         result.append(-1)
#     stack2.append(temp)

# print(*result[::-1])

N = int(input())
numbers = list(map(int, input().split()))

NGE = [-1] * N
stack = []

for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        NGE[stack.pop()] = numbers[i]
    stack.append(i)

print(*NGE)

