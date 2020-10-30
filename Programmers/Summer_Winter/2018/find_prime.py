from itertools import combinations


def solution(nums):
    # My Solution
    comb = combinations(nums, 3)
    arr = []
    mx = 0
    for c in comb:
        tmp = sum(c)
        if mx < tmp:
            mx = tmp
        arr.append(tmp)

    check = [False, False] + [True] * (mx - 1)
    for i in range(2, int(mx**0.5 + 1.5)):
        if check[i]:
            check[2*i::i] = [False] * ((mx - i) // i)

    cnt = 0
    for x in arr:
        if check[x]:
            cnt += 1
    return cnt 


def solution2(nums):
    comb = combinations(nums, 3)
    cnt = 0
    for c in comb:
        csum = sum(c)
        for i in range(2, int(csum**0.5 + 1.5)):
            if csum % i == 0:
                break
        else:
            cnt += 1
        
    return cnt 


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

print(solution2([1,2,3,4]))
print(solution2([1,2,7,6,4]))