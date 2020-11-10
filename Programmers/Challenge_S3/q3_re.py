from collections import Counter


def solution(a):
    answer = 0 
    counter = Counter(a)
    max_num, _ = max(counter.items(), key=lambda x: x[1])

    i = 0
    while i < len(a) - 1:
        if a[i] != max_num and a[i + 1] != max_num:
            i += 1
            continue
        if a[i] == max_num and a[i + 1] == max_num:
            i += 1
            continue
        answer += 2
        i += 2

    return answer


# print(solution([0, 2]))
# print(solution([5,2,3,3,5,3,4]))

# print(solution([0]))
print(solution([5,2,3,3,5,3]))
# print(solution([0,3,3,0,7,2,0,2,2,0]))