#sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
#sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

import heapq

def solution(sizes):
    max_w_heap = []  # 가로 길이를 저장할 최대 힙
    max_h_heap = []  # 세로 길이를 저장할 최대 힙

    for w, h in sizes:
        w, h = max(w, h), min(w, h)  # 항상 w >= h가 되도록 정렬
        heapq.heappush(max_w_heap, -w)  # 최대값을 찾기 위해 음수로 저장
        heapq.heappush(max_h_heap, -h)  # 최대값을 찾기 위해 음수로 저장

    max_w = -heapq.heappop(max_w_heap)  # 최대 가로 길이
    max_h = -heapq.heappop(max_h_heap)  # 최대 세로 길이

    return max_w * max_h