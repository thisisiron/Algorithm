import sys
from collections import deque
input = sys.stdin.readline


def main():
    n = int(input())
    dp = [0, 1, 2] + [0] * (n - 2) 

    if n <= 2:
        print(dp[n])
        return

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n] % 10007)
    return


if __name__ == '__main__':
    main()