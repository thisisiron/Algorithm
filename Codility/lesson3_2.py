
# A[0] = 2, A[1] = 3, A[2] = 1, A[3] = 5 라는 A 리스트가 있을 경우
# 빠진 숫자의 정보를 알고 싶을 때, 단순하게 1부터 len(A)까지 합을 구하고
# 거기에 A리스트의 값들을 모두 더한 값을 빼면 빠진 숫자에 대해 알 수 있음.

def solution(A):
    return sum(range(1, len(A)+2)) - sum(A)

print(solution([2,3,1,5]))