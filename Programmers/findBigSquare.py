# 가장 큰 정사각형 찾기
# From: https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3#
#

def solution(board):
    answer=0
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] != 0 and board[i+1][j]!=0 and board[i][j+1]!=0 and board[i+1][j+1]:
                board[i+1][j+1] = min(board[i][j],board[i+1][j],board[i][j+1]) + 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            answer = max(answer, board[i][j]**2)
                
    return answer

# 9
print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
# 4
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
# 9 
print(solution([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]]))

# 10번 줄에서 min을 사용하게 된 것은 min을 사용하지 않고
# 해결하면 3번 테스트 케이스에 걸리게 된다.
# 1 1 1 0
# 1 2 2 0
# 1 2 3 1    기존의 방법을 사용하면 4,4가 4가 되버린다.
# 0 0 1 4    원래는 1이 되어야 하는데 이것을 해결하기 위해 min을 사용하였다.


# 모범 답안
# def findLargestSquare(board):
#     answer = 1
#     res = [[1 if x=='O' else 0 for x in y] for y in board]
#     for y in range(len(board)):
#         for x in range(len(board[y])):
#             if board[y][x] == 'O':
#                 res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
#                 if res[y][x] > answer: answer = res[y][x]

#     return answer ** 2

# 이 풀이가 좋았던 것은 for문 2개로만 다 해결하였다.
# 마지막에 있는 if문을 이용해서 한 번에 처리하였다.