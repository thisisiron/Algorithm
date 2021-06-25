import sys
from collections import defaultdict 
input = sys.stdin.readline


trees = defaultdict(lambda: 0)
total = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    total += 1

for tree in sorted(trees.keys()):
    print(f"{tree} {(trees[tree] / total) * 100:.4f}")