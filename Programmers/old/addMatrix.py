# 행렬의 덧셈
# From: https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
#

def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))