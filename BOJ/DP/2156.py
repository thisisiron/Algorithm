import sys
input = sys.stdin.readline


def main():
    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]

    if n == 1 or n == 2:
        print(sum(arr))
        return

    ans = [0 for _ in range(n + 1)]
    ans[1] = arr[1]
    ans[2] = arr[1] + arr[2]
    for i in range(3, n + 1):
        ans[i] = max(ans[i - 3] + arr[i - 1] + arr[i], ans[i - 2] + arr[i], ans[i - 1])

    print(ans[i])
    return


if __name__ == '__main__':
    main()