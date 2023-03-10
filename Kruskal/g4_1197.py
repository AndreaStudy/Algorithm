import sys
input = sys.stdin.readline

def f_p(p, x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a = f_p(p,a)
    b = f_p(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

V, E = map(int, input().split())
edges = []
for i in range(E):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

p = [i for i in range(V+1)]
result = 0
for c, a, b in edges:
    if f_p(p,a) != f_p(p,b):
        union(p, a, b)
        result += c

print(result)