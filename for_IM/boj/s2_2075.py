import sys

n = int(input())
l = []

for _ in range(n):
    l += list(map(int,sys.stdin.readline().split()))
    l = sorted(l,reverse=True)[:n]

print(l[-1])

