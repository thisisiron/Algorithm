def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    skill = list(skill)

    for skill_tree in skill_trees:
        cur: int = 0
        right: bool = True 

        for st in skill_tree:
            if st in skill:
                if st != skill[cur]:
                    right = False 
                    break
                else:
                    cur += 1
            if cur == len(skill):
                break
            
        if right:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CEF"]))
    # print(solution("CBD", ["CEF"]))