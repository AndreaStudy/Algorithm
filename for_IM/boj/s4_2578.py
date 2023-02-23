import sys
input = sys.stdin.readline

arr1 = [list(map(int,input().split()))for i in range(5)]
arr2 = list(map(list,zip(*arr1)))

arr3 = []
arr4 = []
for i in range(len(arr1)) :
    arr3.append(arr1[i][i]) 
    arr4.append(arr2[i][4-i]) 
arr = arr1+arr2
arr.append(arr3)
arr.append(arr4) 

lst = []
for i in range(5) :
    lst += list(map(int,input().split())) 
n = 0
for i in lst :
    n +=1
    cnt = 0
    for j in arr :
        if i in j :
            j.remove(i) 
        if j == [] : 
            cnt +=1
    if cnt >= 3: 
        break
print(n) 