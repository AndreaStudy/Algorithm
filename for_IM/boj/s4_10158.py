import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

nx = (p + time) // w
ny = (q + time) // h

if nx % 2 == 0:
    x = (p + time) % w
else:
    x = w - (p + time) % w

if ny % 2 == 0:
    y = (q + time) % h
else:
    y = h - (q + time) % h

print(x, y)