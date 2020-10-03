# 핸드폰 번호 가리기
# From : https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
#

def solution(phone_number):
    answer = ''
    answer = len(phone_number[:-4]) * '*' + phone_number[-4::]
    return answer

print(solution('01011112222'))
print(solution('001029123333'))