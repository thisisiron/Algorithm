import sys
input = sys.stdin.readline


R, C = map(int, input().split())
table = []
for r in range(R):
    table.append(list(input()))
cnt = 0

left, right = 1, R - 1
while left <= right:
    mid = (left + right) // 2
    s = set()

    check = True

    for i in range(C):
        tmp = ''
        for j in range(mid, R):
            tmp += table[j][i]

        if tmp not in s:
            s.add(tmp)
        else:
            check = False
            break
    
    if check:
        left = mid + 1
    else:
        right = mid - 1

print(left - 1)