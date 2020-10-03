def solution_2(N: int, stages: list):
    stages.sort()
    answer: list = [[i + 1, i + 1] for i in range(N)]
    mx: int = 0
    for i in range(1, N + 1):
        idx = 0
        while idx < len(stages) and i == stages[idx]:
            idx += 1
        fail_rate = len(stages[:idx]) / (len(stages) + 1e-8)
        answer[i - 1][1] = fail_rate
        del stages[:idx]
    answer = sorted(answer, key=lambda x: (x[1]), reverse=True)
    return [x[0] for x in answer]


from collections import Counter


def solution(N: int, stages: list):
    answer: list = []
    person: int = len(stages)
    st: Counter = Counter(stages)
    for i in range(1,N+1):
        k: int = st[i]
        if person==0: 
            answer.append([0,i])
        else:
            answer.append([k / person+0.00001, i])
            person -= k
    answer.sort(key=lambda l:l[0], reverse=True)
    return [x[1] for x in answer]


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
    print(solution(4, [4,4,4,4,4]))  # [4,1,2,3]