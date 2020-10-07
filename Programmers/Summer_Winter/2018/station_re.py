import math


def solution(n, stations, w):
    distances = [] 
    for i in range(1, len(stations)):
        distances.append(((stations[i] - 1 - w) - (stations[i - 1] + w)))
    distances.append((stations[0] - 1 - w))
    distances.append((n - (stations[-1] + w)))

    mx_range = 2 * w + 1
    answer = 0
    for dist in distances:
        if dist <= 0:
            continue
        answer += math.ceil(dist / mx_range)

    return answer 


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))