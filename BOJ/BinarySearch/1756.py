import sys
input = sys.stdin.readline


def search(arr, val, end):
    start = 0

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            end = mid 
        else:
            start = mid + 1
    return end


D, N = map(int, input().split())
oven = []
for x in map(int, input().split()):
    if len(oven) > 0:
        if oven[-1] > x:
            oven.append(x)
        else:
            oven.append(oven[-1])
    else:
        oven.append(x)

idx = len(oven)
for x in map(int, input().split()):
    idx = search(oven, x, idx)
    idx -= 1
    if idx < 0:
        break
print(idx + 1)