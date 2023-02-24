import sys
input = sys.stdin.readline

N = int(input())
word = list(map(int, input().split()))

max_length = 1
min_length = 1

a_cnt = 1
i_cnt = 1

result = 0
for i in range(N-1):
    if word[i] >= word[i+1]:
        i_cnt += 1
    else:
        min_length = max(i_cnt, min_length)
        i_cnt = 1
    if word[i] <= word[i+1]:
        a_cnt += 1
    else:
        max_length = max(a_cnt, max_length)
        a_cnt = 1
    
result = max(i_cnt, a_cnt, max_length, min_length)
    

print(result)