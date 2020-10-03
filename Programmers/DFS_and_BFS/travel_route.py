from collections import deque
import copy
import bisect


def solution(tickets):
    check = {}
    for a, b in tickets:
        if a in check:
            bisect.insort(check[a], b)
        else:
            check.setdefault(a, []).append(b)

    stack = deque() 
    stack.append('ICN')
    visited = []

    while stack:
        start = stack[-1]
        if start not in check or len(check[start]) == 0:
            visited.append(stack.pop())
        else:
            stack.append(check[start][0])
            check[start].pop(0)
    return visited[::-1]

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))  # [ICN, A, D, B, A, C]