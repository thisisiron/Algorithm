from collections import deque


def solution(words: list, queries: list) -> list:
    answer: list = []
    trie: Trie = Trie()
    reversed_trie: Trie = Trie()
    for word in words:
        trie.add(word)
        reversed_trie.add(word, use_reverse=True) 
    
    check_dict = {}
    for query in queries:
        if query not in check_dict:
            if query[0] == '?':
                answer.append(reversed_trie.count(query[::-1]))
            else:
                answer.append(trie.count(query))
            check_dict[query] = answer[-1]
        else:
            answer.append(check_dict[query])

    return answer


class Node(object):
    def __init__(self, ch):
        self.ch = ch
        self.length = 0 
        self.children = {}


class Trie(object):
    def __init__(self):
        self.check_list = {}
        self.head: Node = Node(None)

    def add(self, word: str, use_reverse: bool = False):
        if use_reverse:
            word = word[::-1]

        if word not in self.check_list.keys():
            self.check_list[word] = len(word)
            cur: Node = self.head

            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node(ch)
                cur = cur.children[ch]
            cur.length = len(word) 
    
    def count(self, word: str) -> int:
        cur: Node = self.head
        cnt: int = 0
        num_Q: int = word.count('?')

        if num_Q == len(word):
            for len_word in self.check_list.values():
                if len_word == num_Q:
                    cnt += 1
            return cnt

        for ch in word:
            try:
                if ch == '?':
                    stack = deque()

                    for node in cur.children.values():
                        stack.append((node, 1))

                    while stack:
                        cur, cur_depth = stack.pop()

                        if cur.length == len(word) and cur_depth == num_Q:
                            cnt += 1

                        if cur_depth < num_Q:
                            for node in cur.children.values():
                                stack.append((node, cur_depth + 1))
                else:
                    cur = cur.children[ch]
            except KeyError as e:
                break

        return cnt


if __name__ == '__main__':
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))