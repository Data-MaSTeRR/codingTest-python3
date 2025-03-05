import heapq
import sys

n = int(sys.stdin.readline())

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
            heapq.heappush(heap, (abs(i), i))


solution(n)
