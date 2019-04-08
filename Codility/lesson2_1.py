# This solution's point is 87%
def solution(A, K):
    if K==0: return A
    
    if len(A) == 0:
        return A

    for i in range(K):
        tmp = A.pop()
        A.insert(0, tmp)
    
    return A



print(solution([3,8,9,7,6], 3))
print(solution([1,2,3,4], 4))
print(solution([], 0))