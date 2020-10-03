def solution(key: list, lock: list):
    answer: bool = False 

    key_90: list = rotate_90(key)
    key_180: list = rotate_90(key_90)
    key_270: list = rotate_90(key_180)

    cnt_0: int = pad_and_count(key, lock)

    for l_row in range(len(lock) - len(key) + 1):
        for l_col in range(len(lock[0]) - len(key) + 1):
            cnt: int = 0
            for i in range(len(key)):
                for j in range(len(key[0])):
                    if lock[l_row + i][l_col + j] == 0:
                        cnt += 1

            if cnt == cnt_0:
                for rotated_key in [key, key_90, key_180, key_270]:
                    num_key: int = cnt_0 
                    move: bool = False
                    for i in range(len(rotated_key)):
                        for j in range(len(rotated_key[0])):
                            if rotated_key[i][j] == 1 and lock[l_row + i][l_col + j] == 1:
                                move = True 
                                break
                            if rotated_key[i][j] == 1 and lock[l_row + i][l_col + j] == 0:
                                num_key -= 1
                        if move:
                            break
                    
                    if num_key == 0:
                        answer = True
                        return answer
    return answer

def pad_and_count(key: list, lock: list) -> int:
    cnt = 0    
    for i in range(len(lock)):
        cnt += lock[i].count(0)
        lock[i] = [2] * (len(key[0]) - 1) + lock[i] + [2] * (len(key[0]) - 1)
    
    for i in range(len(key) - 1):
        lock.insert(0, [2] * len(lock[0]))

    for i in range(len(key) - 1):
        lock.append([2] * len(lock[0]))
    
    return cnt


def rotate_90(key: list) -> list:
    return [list(reversed(x)) for x in zip(*key)]


def print_matrix(matrix: list):
    for x in matrix:
        print(*x, sep=" ")


if __name__ == '__main__':
    key: list = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock: list  = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
    key: list = [[1, 1], [1, 1]]
    lock: list  = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(solution(key, lock))
    key: list = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock: list  = [[1, 1, 1], [1, 1, 0], [0, 0, 1]]
    print(solution(key, lock))
    key: list = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock: list  = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution(key, lock))