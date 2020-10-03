def solution_2(food_times: list, k: int) -> int:
    answer: int = 0
    index: int = 0
    for sec in range(k):
        check: int = 0

        while food_times[index % len(food_times)] <= 0:
            index += 1
            check += 1
            if check == len(food_times):
                return -1

        if food_times[index % len(food_times)] > 0:
            food_times[index % len(food_times)] -= 1
            index += 1

    check: int = 0
    while food_times[index % len(food_times)] <= 0:
        index += 1
        check += 1
        if check == len(food_times):
            return -1
    return index % len(food_times) + 1

from queue import PriorityQueue


def solution(food_times: list, k: int) -> int:
    if sum(food_times) <= k:
        return -1

    q: PriorityQueue = PriorityQueue()
    for idx, time in enumerate(food_times, 1):
        q.put((time, idx))
    
    sum_val: int = 0
    prev: int = 0
    length: int = len(food_times)
    while sum_val + ((q.queue[0][0] - prev) * length) <= k: 
        now = q.get()[0]
        sum_val += (now - prev) * length
        prev = now
        length -= 1
    result: list = sorted(q.queue, key=lambda x: x[1])
    return result[(k - sum_val) % length][1]


if __name__ == '__main__':
    print(solution([3, 1, 2], 5))  # 1
    print(solution([0, 0, 0], 2))  # -1
    print(solution([2, 3, 1], 6))  # -1
    print(solution([3,1,1,1,2,4,3],12))  # 6