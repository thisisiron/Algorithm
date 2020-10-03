def solution(numbers: list, hand: str) -> str:
    answer = ''
    pad: dict = {}
    k: int = 1
    for i in range(3):
        for j in range(3):
            pad[k] = (i, j)
            k += 1
    pad['*'] = (3,0)
    pad[0] = (3,1)
    pad['#'] = (3,2)

    l_loc = '*'
    r_loc = '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l_loc = number 
        elif number in [3, 6, 9]:
            answer += 'R'
            r_loc = number
        elif number in [2, 5, 8, 0]:
            y, x = pad[number]
            ly, lx = pad[l_loc]
            ry, rx = pad[r_loc]
        
            print(number, l_loc, r_loc, cal_dist(ly, lx, y, x), cal_dist(ry, rx, y, x))
            if cal_dist(ly, lx, y, x) < cal_dist(ry, rx, y, x):
                answer += 'L'
                l_loc = number 
            elif cal_dist(ly, lx, y, x) > cal_dist(ry, rx, y, x):
                answer += 'R'
                r_loc = number
            else:
                if hand == 'right':
                    answer += 'R'
                    r_loc = number
                else:
                    answer += 'L'
                    l_loc = number 

    return answer


def cal_dist(y2, x2, y1, x1) -> float:
    # return ((y2 - y1)**2 + (x2 - x1)**2)**0.5
    return abs(y2 - y1) + abs(x2 - x1)


if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([4,5,0], "right"))
    print(solution([1,2,9,5], "right"))
    print(solution([1,3,5,8,5], "right"))
    print(solution([1,2,9,5], "right"))
    print(solution([2,4,9,8,2], "right"))