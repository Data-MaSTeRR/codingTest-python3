from collections import deque
import sys

N = int(sys.stdin.readline())
s = [ i for i in range(1, N+1)]
print(s)

# 맨 앞 카드 하나 지우고, 그 다음 카드 맨 뒤로 보내기 반복. 마지막에 남는 카드는?
def solution(s):
    dq = deque(s)

    if len(dq) == 1:
        return dq[0]

    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())

    return dq[0]

print(solution(s))
