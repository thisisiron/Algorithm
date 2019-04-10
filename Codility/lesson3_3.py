def solution1(A): # 53%
    mn = 100000 * 1000 + 1000
    for i in range(1, len(A)):
        mn = min(abs(sum(A[:i]) - sum(A[i:])), mn)

    return mn

def solution(A):
    sum_left = 0
    sum_right = sum(A)
    mn = 100000 * 1000 + 1000

    for i in range(1,len(A)):
        sum_left += A[i-1]
        sum_right -= A[i-1]
        mn = min(mn, abs(sum_left - sum_right))

    return mn


print(solution([3,1,2,4,3]))
print(solution([5000,4]))
print(solution([-20, -10]))
print(solution([-10, 10]))