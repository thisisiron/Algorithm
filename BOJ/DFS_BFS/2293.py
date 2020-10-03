import sys


if __name__ == '__main__':
    n: int
    k: int
    n, k = map(int, sys.stdin.readline().rstrip().split())

    coins: list = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline().rstrip()))

    dp: list = [0] * (k + 1)
    dp[0] = 1
    
    coin: int
    for coin in coins:
        j: int
        for j in range(coin, k + 1):
            dp[j] += dp[j - coin]
            print(dp)
        print()
    
    print(dp[k])