import sys 
import heapq
input = sys.stdin.readline


N = int(input())
numbers = []
for _ in range(N):
    tmp = sorted([int(x) for x in input().split()] + numbers, reverse=True)
    numbers = tmp[:N]

print(numbers[N - 1])