import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 순서를 정해줄 함수
def DFS(R):
    # 바깥에 선언한 변수 count를 내에서도 쓸꺼기 때문에 전역변수 선언
    global count
    # 방문처리
    visited[R] = count
    # 작은 순서대로 방문할꺼기 때문에 정렬
    arr[R].sort(reverse=True)
    # 큰 숫자부터 방문
    for i in arr[R]:
        # 방문하지 않았다면
        if visited[i] == 0:
            # 순서를 넣어주고 해당 도착 노드번호로 DFS호출
            count += 1
            DFS(i)

# 정점 N, 간선 M, 시작 노드 R 입력
N, M, R = map(int, input().split())
# 방문처리할 리스트
visited = [0]*(N+1)
# 간선의 정보 저장
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
# 순서를 입력해줄 변수
count = 1
# 함수호출
DFS(R)

# 0번은 편의상 넣은거기 때문에 1번부터 방문순서 호출
# 방문하지 않았다면 초기값 0이 들어가 있음
for i in range(1, N + 1):
    print(visited[i])