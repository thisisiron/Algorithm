def solution(stones: list, k: int) -> int:
    right: int = 200000000 
    left: int = 0

    while left <= right:
        mid: int = (left + right) // 2

        if check_stone(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer + 1


def check_stone(stones: list, k: int, mid: int) -> bool:
    continuous: int = k 
    for stone in stones:
        if stone - mid <= 0:
            continuous -= 1
            if continuous == 0:
                return False 
        else:
            continuous = k 

    return True 

if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))