def solution(n, stations, w):
    coverage = [0] * n

    for station in stations:
        left = station - 1 - w
        right = station + w
        for i in range(left, right):
            if i < 0 or i >= n:
                break
            coverage[i] = 1

    mx_cover = right - left

    cnt = 0
    i = 0 
    while i < n:
        empty = 0
        while empty < mx_cover and coverage[i] != 1:
            if coverage[i] == 0:
                empty += 1
            i += 1
        if empty != 0:
            cnt += 1
        else:
            i += 1

    return cnt 


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))