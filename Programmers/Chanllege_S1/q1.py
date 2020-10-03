def solution(numbers: list) -> list:
    answer: list = []
    for i, i_num in enumerate(numbers):
        for j, j_num in enumerate(numbers):
            if i == j:
                continue
            result: int = i_num + j_num
            if result not in answer:
                answer.append(result)
    return sorted(answer)


if __name__ == '__main__':
    print(solution([2,1,3,4,1]))
    print(solution([5,0,2,7]))