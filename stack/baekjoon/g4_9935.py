import sys
input = sys.stdin.readline


# 시간초과.....
# word = list(input().rstrip())
# bomb = input().rstrip()

# for i in range(len(word)-1,-1,-1):
#     if word[i] in bomb:
#         del word[i]

# if word == []:
#     print('FRULA')
# else:
#     print(''.join(word))


stack = []
word = input().rstrip()
bomb = input().rstrip()

for i in word:
    stack.append(i)
    if stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if not stack:
    print('FRULA')
else:
    print(''.join(stack))