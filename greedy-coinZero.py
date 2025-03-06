import sys

n, coinSum = map(int, input().split())
coinList = [ int(sys.stdin.readline().rstrip()) for _ in range(n) ]

def solution(n, coinSum, coinList):

    reverseCoinList = sorted(coinList, reverse=True)

    coinCnt = 0
    remainSum = coinSum
    for coin in reverseCoinList:

        # 더 이상 동전의 합이 없으면, 중지
        if remainSum == 0:
            break

        # 동전의 합보다 동전가격이 비싸서 다음 동전으로 넘어감
        if coin > coinSum:
            continue

        # 동전의 개수 구하기 알고리즘
        coinCnt += remainSum // coin
        remainSum = remainSum % coin

        #print(f'coin: {coin}, coinCnt: {coinCnt}, remainSum: {remainSum}')

    return coinCnt

print(solution(n, coinSum, coinList))