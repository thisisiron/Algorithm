import sys
input = sys.stdin.readline


N = int(input())
alphabets = {}
for i in range(N):
  row = list(str(input())[:-1])
  for j in range(len(row)):
      alphabets.setdefault(row[j], 0)
      alphabets[row[j]] += 10 ** (len(row) - j - 1)

x = sorted(alphabets.items(), key=lambda x: x[1], reverse=True)
total = 0
for i in range(9, 9-len(x), -1):
    total += i * x[9-i][1]
print(total)