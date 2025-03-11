import sys

N, L = map(int, input().split())

coord = [False] * 1001
for _ in range(N):
    coord[int(sys.stdin.readline())] = True

def solution(N, L, coord):
    sorted_l = sorted(l)

