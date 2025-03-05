from itertools import combinations
import sys

#l = []
#for _ in range(9):
#   l.append(int(sys.stdin.readline().rstrip()))

l = [ int(sys.stdin.readline().rstrip()) for _ in range(9) ]

# 9명의 난쟁이 중 7명의 난쟁이의 합이 100인 난쟁이 오름차순으로 출력
def solution(l):
    sevenDwarf = []
    for comb in combinations(l, 7):
        if sum(comb) == 100:
            sevenDwarf = comb
            break

    sevenDwarf = sorted(list(sevenDwarf)) # combinations는 tuple로 출력

    for dwarf in sevenDwarf:
        print(dwarf)

solution(l)