def solution(people: list, limit: int) -> int:
    answer: int = len(people) 
    
    people.sort(reverse=True)
    start: int = 0
    end: int = len(people) - 1

    while start < end:
        if people[start] + people[end] <= limit:
            end -= 1
            answer -= 1
        start += 1

    return answer 


if __name__ == '__main__':
    print(solution([70, 50, 80, 50],100))
    print(solution([70, 80, 50],100))