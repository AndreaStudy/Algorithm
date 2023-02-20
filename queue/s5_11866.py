import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

queue = deque(list(range(1,N+1)))
result = []

while queue:
    if len(queue) >= 2:
        for _ in range(M-1):
            queue.append(queue.popleft())
        result.append(str(queue.popleft()))
    else:
        result.append(str(queue.popleft()))

print("<",end="")
print(", ".join(result),end=">")
