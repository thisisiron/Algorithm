# 숫자의 표현
# From: https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3
#

# 해당 솔루션 시간초과
# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             sum_number = sum(range(i,j+1))
#             if sum_number == n:
#                 answer+=1
#                 break
#     return answer


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1
    return answer


print(solution(15))

# for문을 단지 2개 사용하는 것보다
# while문을 이용해서 사용하는 것이 더 빠르다.

# 1번째 솔루션 성능
# 테스트 1 〉	통과 (0.17ms)
# 테스트 2 〉	통과 (588.40ms)
# 테스트 3 〉	통과 (254.16ms)
# 테스트 4 〉	통과 (277.45ms)
# 테스트 5 〉	통과 (14.70ms)
# 테스트 6 〉	통과 (0.40ms)
# 테스트 7 〉	통과 (198.98ms)
# 테스트 8 〉	통과 (43.29ms)
# 테스트 9 〉	통과 (0.93ms)
# 테스트 10 〉	통과 (1298.48ms)
# 테스트 11 〉	통과 (1303.51ms)
# 테스트 12 〉	통과 (341.21ms)
# 테스트 13 〉	통과 (379.75ms)
# 테스트 14 〉	통과 (212.85ms)

# 2번째 솔루션 성능
# 테스트 1 〉	통과 (0.14ms)
# 테스트 2 〉	통과 (0.34ms)
# 테스트 3 〉	통과 (0.28ms)
# 테스트 4 〉	통과 (0.29ms)
# 테스트 5 〉	통과 (0.17ms)
# 테스트 6 〉	통과 (0.15ms)
# 테스트 7 〉	통과 (0.27ms)
# 테스트 8 〉	통과 (0.21ms)
# 테스트 9 〉	통과 (0.14ms)
# 테스트 10 〉	통과 (0.40ms)
# 테스트 11 〉	통과 (0.40ms)
# 테스트 12 〉	통과 (0.30ms)
# 테스트 13 〉	통과 (0.30ms)
# 테스트 14 〉	통과 (0.27ms)