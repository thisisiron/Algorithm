from collections import deque


def solution(a: list) -> int:
    result: set = set()
    small: bool = False
    stack: deque = deque()

    stack.append([a.copy(), small])
    
    while stack:
        print(len(stack))
        a, small = stack.pop()
        if len(a) == 1:
            result.add(a[0])
            continue

        for idx in range(len(a) - 2, -1, -1):
            if a[idx] < a[idx + 1]:
                small_idx: int = idx
                large_idx: int = idx + 1
            else:
                small_idx: int = idx + 1
                large_idx: int = idx

            x_list: list = a.copy()
            del x_list[large_idx]
            stack.append([x_list, small])

            if small == False:
                x_list: list = a.copy()
                del x_list[small_idx]
                stack.append([x_list, True])

    return len(result) 


if __name__ == '__main__':
    print(solution([9,-1,-5]))
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))