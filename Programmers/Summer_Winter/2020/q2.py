from collections import deque


def solution(encrypted_text, key, rotation):
    answer = ''
    rotated = deque(encrypted_text)
    rotated.rotate(-rotation)
    for i, t in enumerate(rotated):
        k_n = ord(key[i]) - 96
        t_n = ord(t) - 97
        res = t_n - k_n
        if res < 0:
            res += 26
        # print(f'{t_n}({rotated[i]}) - {k_n}({key[i]}) = {res}({chr(res + 97)})')
        answer += chr(res + 97)
    return answer


print(solution('qyyigoptvfb', 'abcdefghijk', 3))
print(solution('xafzy', 'gbaaa', -3))
print(solution('bac', 'dbc', 0))