from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x:
        heappush(heap, -x)
    else:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
