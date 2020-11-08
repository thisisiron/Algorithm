def solution(s):
    iter_cnt = 0
    zero_cnt = 0
    while s != '1':
        tmp = ""
        for x in s:
            if x == '0':
                zero_cnt += 1
            else:
                tmp += x
        s = bin(len(tmp))[2:]
        iter_cnt += 1

    return [iter_cnt, zero_cnt] 


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))