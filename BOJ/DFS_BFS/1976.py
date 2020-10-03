import sys


def find_parent(x: int, parent: dict) -> int:
    if x == parent[x]:
        return x
    else:
        p: int = find_parent(parent[x], parent)
        parent[x] = p
        return p


def union_find(x: int, y: int, parent: dict):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    parent[y] = x


if __name__ == '__main__':
    total_city: int = int(sys.stdin.readline().rstrip())
    travel_city: int = int(sys.stdin.readline().rstrip())

    parent: dict = {i: i for i in range(1, total_city + 1)}

    for i in range(1, total_city + 1):
        x = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(1, len(x) + 1):
            if x[j - 1] == 1:
                union_find(i, j, parent)

    plan: list = list(map(int, sys.stdin.readline().rstrip().split()))
    result: set = set([find_parent(p, parent) for p in plan])  # parent[p]를 바로 사용하면 틀림 (재귀로 union-find 구현시 발생하는 문제)

    if len(result) != 1:
        print("NO")
    else:
        print("YES")