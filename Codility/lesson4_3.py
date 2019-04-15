def solution(N, A):
    X = [0] * N
    mx = 0
    next_mx = 0
    for a in A:
        if a > N:
            mx = next_mx
        else:
            X[a-1] = max(X[a-1]+1, mx+1)
            next_mx = max(X[a-1], next_mx)
    return [x if x>mx else mx for x in X]

print(solution(5, [3,4,4,6,1,4,4])) # [3, 2, 2, 4, 2]