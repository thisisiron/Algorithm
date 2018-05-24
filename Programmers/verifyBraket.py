#
# From : https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3
#

def solution(s):
    if s.count('(') != s.count(')'): return False
    braket = []
    for i in range(len(s)):
        if s[i] == '(':
            braket.append(s[i])
        elif s[i]==')' and braket==[]:
            return False
        elif s[i] ==')' and braket[-1]=='(':
            braket.pop()
    return braket==[]

print(solution('(()('))
print(solution('()(())'))

# 모범 답안
# Index error발생을 try catch문으로 해결하는 방법을 사용했다.

# def is_pair(s):
#     st = list()
#     for c in s:
#         if c == '(':
#             st.append(c)

#         if c == ')':
#             try:
#                 st.pop()
#             except IndexError:
#                 return False

#     return len(st) == 0