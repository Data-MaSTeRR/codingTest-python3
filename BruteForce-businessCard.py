#sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
#sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    # index 0에 큰 수가 오게하기
    sorted_list = []
    for front, back in sizes:
        if front < back:
            sorted_list.append([back, front])
        else:
            sorted_list.append([front, back])

    # 정렬한 리스트에서 index 0, 1의 최댓값 각각 구하기
    max_front, max_back = 0, 0
    for front, back in sorted_list:
        if max_front < front:
            max_front = front

        if max_back < back:
            max_back = back

    # index 0에서 가장 큰 값 x index 1에서 가장 큰 값
    answer = max_front * max_back

    return answer