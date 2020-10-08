def solution(a):
    if len(a) <= 2:
        return len(a)
    rest = 2
    left = a[0]
    right = a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
            rest += 1
            print('left', a[i])
        if right > a[-1 - i]:
            right = a[-1 - i]
            rest += 1
            print('right', a[-1 - i])

    if left == right:
        return rest - 1
    else:
        return rest


if __name__ == '__main__':
    print(solution([9,-1,-5]))
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))