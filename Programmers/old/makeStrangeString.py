def solution(s):
    return " ".join(["".join([letter.upper() if i%2==0 else letter.lower() for i,letter in enumerate(word)]) for word in s.split(" ")])


print(solution("try hello world"))
print(solution("Hi   my   name"))

# 모범 답안
# 공백이 2개일 경우 내가 작성한 Solution으로는 해결할 수 없다.
# 그러므로 split함수를 사용할 때 
# split()   ->   split(" ") 이렇게 고쳐준다면 공백이 2개이상이어도 처리가능하다.