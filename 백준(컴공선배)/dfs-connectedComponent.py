import sys

input = sys.stdin.readline # 입력을 빠르게 받기
sys.setrecursionlimit(10**6) # 재귀하는 한도 늘리기

# 노드, 간선의 개수 입력받기
N, M = map(int, input().split())

# 인접행렬 초기화
adj = [[0] * N for _ in range(N)]
# 인접행렬의 간선 정보 입력받기
for i in range(M):
    a, b = map(lambda x:x-1, map(int, input().split())) # 0~N-1까지의 index
    adj[a][b] = adj[b][a] = 1


answer = 0
chk = [False] * N  # 방문 체크 배열

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] == 1 and chk[nxt] == False: # 만약 now-nxt 사이에 간선이 존재하고, nxt에 방문하지 않았다면
            chk[nxt] = True # 해당 노드와 간선으로 연결되어 있는 것 모두 체크표시
            dfs(nxt)

for i in range(N):
    if chk[i] == False: # 0~N-1까지 보지 않은 것 순회
        answer += 1
        chk[i] = True
        dfs(i) # 해당 노드와 간선으로 연결되어 있는 것 모두 체크표시하러!


print(answer)
