from itertools import permutations

# numbers = "17"
numbers = "011"

def isPrimeN(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    uniqueNumbers = set()
    for i in range(1, len(numbers) + 1):  # 1의 자리부터 len(numbers) 자리까지
        for number in permutations(numbers, i):  # 순열 만들기
            number = int(''.join(number))  # 앞자리 0은 int() 통해 자동으로 제거
            uniqueNumbers.add(number)  # 고유한 숫자로 변환

    answer = [i for i in uniqueNumbers if isPrimeN(i) == True]

    return len(answer)

print(solution(numbers))