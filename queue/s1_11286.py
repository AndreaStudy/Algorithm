from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
p_heap = []
m_heap = []
for i in range(N):
    x = int(input())
    if x > 0:
        heappush(p_heap, x)
    elif x < 0:
        heappush(m_heap, -x)
    else:
        if p_heap and m_heap:
            a = heappop(p_heap)
            b = heappop(m_heap)
            if b <= a:
                print(-b)
                heappush(p_heap, a)
            else:
                print(a)
                heappush(m_heap, b)
        elif p_heap:
            print(heappop(p_heap))
        elif m_heap:
            print(-heappop(m_heap))
        else:
            print(0)
