import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    queue1 = deque(nums)
    idx = list(range(N))
    queue2 = deque(idx)
    cnt = 0

    while queue1:
        if queue1[0] == max(queue1):
            cnt += 1
            if queue2[0] == M:
                print(cnt)
                break
            queue1.popleft()
            queue2.popleft()
        else:
            queue1.append(queue1.popleft())
            queue2.append(queue2.popleft())
