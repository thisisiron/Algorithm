import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        x *= 10000000

        n = int(input())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        arr.sort()

        left = 0
        right = len(arr) - 1
        flag = False
        while left < right:
            cur = arr[left] + arr[right]
            if cur == x:
                flag = True
                break
            elif cur < x:
                left += 1
            else:
                right -= 1
        print('danger' if not flag else f'yes {arr[left]} {arr[right]}')
    except ValueError as e:
        break
