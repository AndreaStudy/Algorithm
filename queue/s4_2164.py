import sys
input = sys.stdin.readline
from collections import deque

N = list(range(1, int(input())+1))
queue = deque(N)
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
