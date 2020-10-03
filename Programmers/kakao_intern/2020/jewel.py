from collections import Counter


def solution(gems: list) -> list:
    kind_gem: int = len(set(gems))
    start: int
    end: int
    start, end = 0, 0 
    answer: list = [start, len(gems) - 1]
    check_box: dict = {gems[0]: 1} 

    while start < len(gems) and end < len(gems):
        if len(check_box.keys()) < kind_gem: 
            end += 1
            if end == len(gems):
                break
            if check_box.get(gems[end]) is None:
                check_box[gems[end]] = 1
            else:
                check_box[gems[end]] += 1
        else:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
            if check_box[gems[start]] == 1:
                del check_box[gems[start]]
            else:
                check_box[gems[start]] -= 1

            start += 1
        # print(start, end)
        # print(check_box, '\n')
    answer[0] += 1
    answer[1] += 1
    return answer


if __name__ == '__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print(solution(["XYZ", "XYZ", "XYZ"]))
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))