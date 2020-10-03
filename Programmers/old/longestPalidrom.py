def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(1, len(s)+1):
            if s[i:j] and s[i:j] == s[i:j][::-1]:
                answer.append(len(s[i:j]))

    return max(answer)

print(solution("abcdcba"))
print(solution("abacde"))