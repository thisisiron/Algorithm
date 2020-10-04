import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n: int = int(input())
    numbers: list = list(map(int, input().split()))

    dp: list = [0] * n
    for i in range(n):
        if dp[i - 1] + numbers[i] > numbers[i]:
            dp[i] = dp[i - 1] + numbers[i]
        else:
            dp[i] = numbers[i]

    print(max(dp))
