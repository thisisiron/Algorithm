def solution(A):
    if len(A)<=1: return 0
    infos = [0] * 6
    for a in A:
        infos[a-1] += 1
    mn =101 
    mn_i = 7
    for i in range(6):
        if mn > infos[5-i] and infos[i]!=0:
            mn = infos[5-i] 
            mn_i = i
    result = 0
    for i in range(6):
        if i != mn_i:
            if i ==(5 - mn_i):
                result += infos[i] * 2
            else:
                result += infos[i]
    return result

# print(solution([1,2,3])) # 2
# print(solution([1,1,6])) # 2
# print(solution([1,6,2,3])) # 3
# print(solution([6,6,6,2,2,1,1])) # 5

import random
# A = [random.randint(1,6) for _ in range(100)]
A = [1, 2, 5, 6, 3, 1, 5, 6, 3, 1, 4, 3, 1, 1, 1, 6, 5, 2, 6, 1, 5, 5, 6, 2, 4, 1, 2, 4, 5, 3, 5, 5, 4, 6, 3, 1, 1, 5, 6, 2, 4, 6, 5, 3, 6, 3, 5, 5, 5, 3, 6, 3, 4, 1, 4, 1, 3, 1, 6, 3, 3, 3, 6, 1, 1, 6, 4, 1, 3, 3, 6, 3, 5, 1, 4, 6, 6, 4, 3, 2, 4, 4, 4, 4, 6, 4, 1, 4, 1, 3, 5, 3, 1, 4, 5, 3, 4, 3, 5, 4]
print(solution(A))