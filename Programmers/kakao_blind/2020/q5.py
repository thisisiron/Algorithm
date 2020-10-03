def solution(n: int, build_frame: list) -> list:
    answer: set = set() 

    for x, y, _type, _oper in build_frame:
        if _oper == 0:  # 삭제
            if (x, y, _type) in answer:
                answer.remove((x, y, _type))
                ok = check(answer)
                if ok:
                    continue
                else:
                    answer.add((x, y, _type))
        elif _oper == 1:
            answer.add((x, y, _type))
            ok = check(answer)
            if ok:
                continue
            else:
                answer.remove((x, y, _type))

    answer = [list(x) for x in answer]
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


def check(components: set) -> bool:
    for x, y, _type in components:
        if _type == 0:  # 기둥
            if y == 0 or (x, y, 1) in components or (x, y - 1, 0) in components or (x - 1, y, 1) in components:
                continue
            else:
                return False 
        elif _type == 1:  # 보
            if (x, y - 1, 0) in components or (x + 1, y - 1, 0) in components or ((x - 1, y, 1) in components and (x + 1, y, 1) in components):
                continue
            else:
                return False 

    return True 


if __name__ == '__main__':
    print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
    print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
    print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[5,0,0,1],[4,1,1,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1], [1,1,1,0], [2,1,1,0], [3,1,1,0], [4,1,1,0], [4,0,0,0], [5,1,0,0], [0,0,0,0]]))