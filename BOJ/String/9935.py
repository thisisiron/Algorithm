import sys
input = sys.stdin.readline


S = input().rstrip()
bomb = input().rstrip()

last_char = bomb[-1]  # 폭발 문자열의 마지막 글자
stack = []

for s in S:
    stack.append(s)
    if s == last_char and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

ans = ''.join(stack)
print(ans if ans else 'FRULA')