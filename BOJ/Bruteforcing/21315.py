import sys
input = sys.stdin.readline


def shuffle(k):
    end = N
    for i in range(1, k + 1 + 1):
        up = 2 ** (k - i + 1)
        new_cards = []
        for j in range(end - up, end):
            new_cards.append(before[j])
            before[j] = 0
        
        for j in range(N):
            if before[j] != 0:
                new_cards.append(before[j])
            before[j] = new_cards[j]
        end = up

N = int(input())
after = [int(x) for x in input().split()]

k1 = 1
while 2**k1 <= N:
    k2 = 1
    while 2**k2 <= N:
        before = [x for x in range(1, N + 1)]

        shuffle(k1)
        shuffle(k2)
        flag = True
        for i in range(N):
            if before[i] != after[i]:
                flag = False
                break
        if flag:
            print(k1, k2)
            exit(0)
        k2 += 1
    k1 += 1