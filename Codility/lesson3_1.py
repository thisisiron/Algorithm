def solution(X, Y, D):
    cnt = 0

    if X==Y:
        return 0

    if (Y - X) % D != 0:
        return ((Y-X)//D) + 1
    else:
        return (Y-X)//D

print(solution(10, 85, 30))
print(solution(10, 10, 5))