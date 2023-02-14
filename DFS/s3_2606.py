import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 전염시킬 함수
def DFS(r):
    # 전염된 컴퓨터의 개수를 세어줄 count변수를 전역변수로 바꿈
    global count
    # 현재 노드 방문처리
    visited[r] = 1
    # 방문할 곳이 있다면
    for i in arr[r]:
        # 방문한적이 없다면
        if visited[i] == 0:
            # 전염시켜버리기
            count += 1
            # i노드에 대해서 다시 DFS
            DFS(i)
# 노드 정보
N = int(input())
# 간선의 개수
K = int(input())
# 간선의 정보 입력
arr = [[] for _ in range(N+1)]
for i in range(K):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
# 방문처리할 리스트
visited = [0] *(N+1)
# 전염된 컴퓨터의 개수
count = 0
# 1번부턴 감염되여 전염
DFS(1)
# 전염된 컴퓨터 개수
print(count)
