from collections import deque


def solution(begin: str, target: str, words: list) -> int:
    if target not in words:
        return 0

    visited = {} 
    stack = deque()
    cnt = 0
    for idx, word in enumerate(words):
        diff = 0
        for a, b in zip(begin, word):
            if a != b:
                diff += 1  
        if diff == 1 and not visited.get(word, False):
            cnt += 1
            stack.append([words[idx], cnt])
            visited[word] = True

    
    while len(stack) != 0:
        cur_word, cnt = stack.pop()

        if cur_word == target: 
            return cnt

        for idx, word in enumerate(words):
            diff = 0
            cur_cnt = cnt
            for a, b in zip(cur_word, word):
                if a != b:
                    diff += 1  
            if diff == 1 and not visited.get(word, False):
                cur_cnt += 1
                stack.append([words[idx], cur_cnt])
                visited[word] = True
        
    return 0
        

if __name__ == '__main__':
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
    print()
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))