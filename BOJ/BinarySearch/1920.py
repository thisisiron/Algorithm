import sys
input = sys.stdin.readline


def search(x_list, val):
    left = 0
    right = len(x_list)

    while left < right:
        mid = (left + right) // 2
        if x_list[mid] < val:
            left = mid + 1
        elif x_list[mid] > val:
            right = mid
        else:
            return mid
    return -1 


N = int(input())
stored = sorted(list(map(int, input().split())))
M = int(input())
searched = list(map(int, input().split()))

for se in searched:
    res = search(stored, se)
    if res == -1:
        print(0)
    else:
        print(1)