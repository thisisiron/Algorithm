import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in map(int, input().split())]
arr.sort()
count = 0
for i in range(N - 2):
    left, right = i + 1, N - 1
    target = -arr[i]
    if target < 0:
        break

    while left < right:
        tmp = arr[left] + arr[right]
        if tmp == target:
            if arr[left] == arr[right]:
                count += (right - left)
                left += 1
            else:
                mx_r = right
                while mx_r >= 0 and arr[right] == arr[mx_r - 1]:
                    mx_r -= 1
                r = (right - mx_r + 1)
                count += r
                mn_l = left
                while mn_l < N and arr[left] == arr[mn_l + 1]:
                    mn_l += 1
                l = (mn_l - left + 1)
                left += l
                right -= r
                count += (l * r)
        elif tmp < target:
            left += 1
        else:
            right -= 1
print(count)