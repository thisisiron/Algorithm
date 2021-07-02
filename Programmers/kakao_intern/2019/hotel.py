from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


def solution(k, room_number):
    room = defaultdict(lambda: 0)
    answer = []
    for n in room_number:
        check = find(room, n)
        answer.append(check)
        room[check] = check + 1
    return answer


def find(room, x):
    if room[x] == 0:
        return x
    else:
        room[x] = find(room, room[x])
        return room[x]


if __name__ == '__main__':
    print(solution(10, [1,3,4,1,3,1]))