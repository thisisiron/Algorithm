def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            if check_sum == X:
                return i
    return -1

print(solution(5, [1,3,1,4,2,3,5,3]))