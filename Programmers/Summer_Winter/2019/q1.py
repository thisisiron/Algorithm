def solution(w: int, h: int) -> int:
    a: int = max(w, h)
    b: int = min(w, h)

    g: int = gcm(a, b)

    return (a * b) - (a + b - g)


def  gcm(a: int, b: int) -> int:
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


if __name__ == '__main__':
    print(solution(8, 12))