import sys

input = sys.stdin.readline()
sys.setrecursionlimit(10**6) # 재귀하는 한도 늘리기

N, M = map(int, input().split())

# 인접행렬 만들기
adj = [[0] * N for _ in range(N)]
for i in range(M):
    a, b = map(lambda x:x-1, map(int, input().split())) # 0~N-1까지의 index
    adj[a][b] = adj[b][a] = 1



