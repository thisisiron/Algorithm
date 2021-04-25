import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def back(coin, cnt):
    if check[coin] >= cnt:
        return
    
    check[coin] = cnt

    if coin == X:
        for i in range(4):
            ans[i] = used[i]
        return

    if coins[0] >= used[0] + 5 and  coin + 5 <= X:
        used[0] += 5
        back(coin + 5, cnt + 5)
        used[0] -= 5
    
    if coins[1] > used[1] and  coin + 5 <= X:
        used[1] += 1
        back(coin + 5, cnt + 1)
        used[1] -= 1

    if coins[2] > used[2] and  coin + 10 <= X:
        used[2] += 1
        back(coin + 10, cnt + 1)
        used[2] -= 1

    if coins[3] > used[3] and  coin + 25 <= X:
        used[3] += 1
        back(coin + 25, cnt + 1)
        used[3] -= 1


coins = [0] * 4
used = [0] * 4
ans = [0] * 4
X, coins[0], coins[1], coins[2], coins[3] = map(int, input().split())
check = [-1] * (X + 1)

x = X % 5
if coins[0] < x:
    print(0, 0, 0, 0)
    exit()

used[0], coin = x, x
back(coin, coin)
print(*ans, sep=" ")