# 땅따먹기
# From: https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
#

# 시간 초과 ( 그리드 알고리즘 )

# def solution(land):
#     answer = 0
#     for row in range(len(land)):
#         m = max(land[row])
#         answer += m
#         for i in range(row+1,len(land)):
#             land[i][land[row].index(m)] = -1            
#     return answer

# 그리드 알고리즘의 문제점은
# | 1 | 2 | 3    | 5 |
# | 5 | 6 | 7    | 8 |
# | 4 | 3 | 1000 | 1 |
# 위와 같을 경우 1000을 고려하지 않게 되는 문제가 발생한다.
# 이것을 해결하기 위해서은 DP로 해결해야 한다.
# 헷갈렸던 것은 하나 줄을 선택하면 다시는 그 줄을 선택할 수 없는 줄 알았다.
# 하지만 단지 연속해서 선택할 수 없을 뿐이었다.

def solution(land):
    answer = 0
    dp = [[0] * len(land[0]) for i in range(len(land))]
    for i in range(len(land[0])):
        dp[0][i] = land[0][i]
    for row in range(1, len(land)):
        for col in range(len(land[0])):
            for k in range(len(land[0])):
                if k!=col:
                    dp[row][col] = max(dp[row-1][k] + land[row][col], dp[row][col])
    answer = max(dp[-1][:])
    return answer

board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(solution(board))


