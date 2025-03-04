import sys

#n = int(input())
#for _ in range(n):
#   s = sys.stdin.readline().split()

s = list(sys.stdin.readline().rstrip())
print(s)

# 괄호의 짝이 알맞게 있는지 확인 -> stack 자료구조 활용
def solution(s):

    stack = []
    flag = True
    for ch in s:
        if ch == '(':
            stack.append(ch)

        if ch == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
                break

    if len(stack) > 0:
        flag = False

    if flag == True:
        return True
    else:
        return False

print(solution(s))



