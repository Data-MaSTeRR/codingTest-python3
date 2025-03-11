
N, L = map(int, input().split())

# True, False 리스트를 사용
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

# 최초 구멍이 있는 곳에 테이프를 붙이고, L만큼 건너뛰고 새로운 구멍을 찾는 알고리즘
def solution(L, coord):
    answer = 0
    i = 0
    while i < 1001:
        if coord[i] == True:
            answer += 1
            i += L
        else:
            i += 1

    return answer

print(solution(L, coord))


