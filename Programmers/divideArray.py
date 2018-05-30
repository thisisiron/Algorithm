#
# From : https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
#

def solution(arr, divisor):
    
    answer = sorted([x for x in arr if x%divisor==0])
    if answer==[]:
        return [-1]
    print(answer)
    return answer

print(solution([5,9,7,10],5))
print(solution([2,36,1,3],1))
print(solution([3,2,6],10))


# 모범 답안

# 리턴에서 if문을 활용하였다.

# def solution(arr, divisor):
#     arr = [x for x in arr if x % divisor == 0];
#     arr.sort();
#     return arr if len(arr) != 0 else [-1];