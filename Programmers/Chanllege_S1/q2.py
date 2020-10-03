def solution(n: int) -> list:
    answer: list = [0] * (sum(range(2, n + 1)) + 1)
    val: int = 0

    num_loop: int = ((n - 1) // 3) + 1
    break_point: int = (n - 1) % 3
    init_idx: int = 0

    for i in range(0, num_loop * 2 - 1, 2):

        idx: int = init_idx + (i + i)
        init_idx = idx
        
        skip: int = i
        for a in range(0, n - 3 * (i // 2)): 
            if a != 0 :
                idx += skip 
            val += 1
            answer[idx] = val
            skip += 1

        if break_point == 0 and i == (num_loop - 1) * 2:
            break

        for b in range(n - 1 - 3 * (i // 2)):
            idx += 1
            val += 1
            answer[idx] = val
        if break_point == 1 and i == (num_loop - 1) * 2:
            break
        
        c: int = n - (i // 2)
        for _ in range(n - 1 - 3 * (i // 2) - 1):
            idx -= c
            val += 1
            answer[idx] = val
            c -= 1
        if break_point == 2 and i == (num_loop - 1) * 2:
            break

    return answer


def print_pyramid(p: list, n: int):
    col: int = 1
    idx: int = 0
    d: int = len(str(max(p)))
    for i in range(n):
        print(" " * (n - i), end="")
        for _ in range(col):
            print(f"{str(p[idx]).zfill(d)}", end=" ") 
            idx += 1
        print()
        col += 1
    print()

if __name__ == '__main__':
    print_pyramid(solution(1), 1)
    print_pyramid(solution(2), 2)
    print_pyramid(solution(3), 3)
    print_pyramid(solution(4), 4)
    print_pyramid(solution(5), 5)
    print_pyramid(solution(6), 6)
    # print_pyramid(solution(7), 7)
    # print_pyramid(solution(8), 8)
    # print_pyramid(solution(9), 9)
    # print_pyramid(solution(10), 10)
    # print_pyramid(solution(11), 11)
    print_pyramid(solution(20), 20)