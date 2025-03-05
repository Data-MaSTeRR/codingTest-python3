import heapq
import sys

n = int(sys.stdin.readline())

# 절댓값 힙
def solution(n):
    heap = []
    for _ in range(n):
        i = int(sys.stdin.readline())
        if i == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            # 절댓값 작은 순으로 min-heap, 실제 출력은 index 1로
            heapq.heappush(heap, (abs(i), i))


solution(n)
