import sys
input = sys.stdin.readline

N = int(input())

atm = list(map(int, input().split()))
atm.sort()

total = 0
temp = 0

for i in range(N):
    temp += atm[i]
    total += temp

print(total)
