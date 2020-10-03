# 2016년
# From : 
#

def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    return day[(sum(month[:a-1]) + b) % 7]

# TUE 화요일이 정답
print(solution(5,24))

# 주의 : 이전 달 일수를 모두 더해야한다.
# 예를 들어 2월이면 31일이지만
# 3월이라면 31 + 29 를 해야한다.