def solution(name):
    a2i = [min(ord(x) - ord("A"), ord("Z") - ord(x) + 1) for x in name]
    idx, answer = 0, 0
    while True:
        answer += a2i[idx]
        a2i[idx] = 0
        if sum(a2i) == 0:
            break
        left, right = 1, 1
        while a2i[idx - left] == 0:
            left += 1
        while a2i[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer