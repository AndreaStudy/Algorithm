import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()

for i in range(N):
    word = input().split()
    if len(word) == 2:
        queue.append(word[-1])
    else:
        if word[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif word[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif word[0] == 'size':
            print(len(queue))
        elif word[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif word[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)