import sys

n = int(sys.stdin.readline())

def solution(n):
    d = {}
    for _ in range(n):
        key = sys.stdin.readline().rstrip()
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    # value 값이 가장 큰 key만 후보자 리스트로
    max_cnt = max(d.values())
    candidate = []
    for k, v in d.items():
        if v == max_cnt:
            candidate.append(k)

    # 동점자가 있으면 알파벳순 오름차순
    candidate.sort()

    return print(candidate[0])


solution(n)