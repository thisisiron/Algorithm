def solution(s):
    answer = len(s) 
    max_len_s = len(s) // 2
    for k in range(1, max_len_s + 1):
        val = compress(s, k)
        if answer > val:
            answer = val
    return answer


def compress(s, k):
    cnt = 1
    i = 0
    compressed_str = ""
    while i < len(s):
        if s[i:i + k] == s[i + k: i + k * 2]:
            cnt += 1
        else:
            if cnt > 1:
                compressed_str += str(cnt) + s[i: i + k]
            else: 
                compressed_str += s[i: i + k]
            cnt = 1
        i += k
    print(compressed_str)
    
    return len(compressed_str) 


if __name__ == '__main__':
    print(solution('aabbaccc'), '\n')
    print(solution('ababcdcdababcdcd'), '\n')


"""
Memo
- aabbaccc가 2개로 자를 때 2a2b
"""