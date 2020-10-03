from collections import deque
from itertools import permutations


def solution(n: int, weak: list, dist: list) -> int:
    answer: int = 0
    dist.sort(reverse=True)
    weak: deque = deque(weak)
    for i in range(1, len(dist) + 1):  # 투입 인원
        if i == 1:
            for _ in range(len(weak)):
                if weak[-1] <= weak[0] + dist[0]:
                    return 1
                else:
                    weak.rotate(-1)
                    weak[-1] += n
            weak = deque([x % n for x in weak])
        else:
            order_dist = list(permutations(dist[:i]))  # i명 투입한다고 가정시 i명에 대한 순열 
            for new_dist in order_dist:
                for _ in range(len(weak)):
                    start = 0
                    for d in new_dist:
                        tmp_start = start
                        weak_location = weak[tmp_start]
                        for x in range(1, d + 1):  # d만큼 갈 수 있는지 체크
                            if tmp_start + 1 >= len(weak):
                                break
                            if weak[tmp_start + 1] == weak_location + x:
                                tmp_start += 1 
                        start = tmp_start + 1
                        if start == len(weak):
                            return i
                    weak.rotate(-1)  # 앞에 녀석을 n(전체길이)만큼 더한 후 맨 뒤로 이동
                    weak[-1] += n
                weak = deque([x % n for x in weak])
    return -1 


if __name__ == '__main__':
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))