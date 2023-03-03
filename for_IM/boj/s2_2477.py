import sys
input = sys.stdin.readline

K = int(input())
max_height = 0  
max_width = 0  
mw_idx = 0  
mh_idx = 0 
arr = []
for i in range(6):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if temp[0] == 1 or temp[0] == 2:  
        if max_width < temp[1]: 
            max_width = temp[1] 
            mw_idx = i 
    else:
        if max_height < temp[1]: 
            max_height = temp[1]  
            mh_idx = i  

idx_list = [arr[mh_idx - 1], arr[(mh_idx + 1) % 6], arr[mw_idx - 1],
              arr[(mw_idx + 1) % 6]]

product = 1  
for i in arr:  
    if i not in idx_list:  
        product *= i[1] 

result = (max_width * max_height - product) * K 
print(result)