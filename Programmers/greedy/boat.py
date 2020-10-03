def solution(people: list, limit: int) -> int:
    people.sort(reverse=True)
    i: int = -1
    cnt: int = 0
    while people:
        a = people[0]
        if len(people) == 1:
            del people[0]
            cnt += 1
            continue
        b = people[-1]
        if a + b <= limit:
            del people[-1]
        del people[0]
        cnt += 1

    return cnt 


if __name__ == '__main__':
    print(solution([70, 50, 80, 50],100))
    print(solution([70, 80, 50],100))