import sys
sys.stdin = open('5639.txt', 'r')
sys.setrecursionlimit(10**9)

nums = list(map(int, sys.stdin.read().split()))
        
def postorder(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if nums[start] < nums[i]:
            mid = i
            break

    postorder(start+1, mid-1) 
    postorder(mid, end)
    print(nums[start])

postorder(0, len(nums)-1)