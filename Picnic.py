# From: https://algospot.com/judge/problem/read/PICNIC

# Input
# 3
# 2 1
# 0 1
# 4 6
# 0 1 1 2 2 3 3 0 0 2 1 3
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5


def countPairngs(n, matched, areFriends):
    firstFree = -1
    for i in range(n):
        if not matched[i]:
            firstFree = i
            break
    if firstFree == -1:
        return 1
    ret = 0
    for j in range(firstFree+1, n):
        if not matched[j] and areFriends[firstFree][j]:
            matched[firstFree] = matched[j] = True
            ret += countPairngs(n, matched, areFriends)
            matched[firstFree] = matched[j] = False
    return ret


if __name__=="__main__":
    result = []
    case = int(input())
    for i in range(case):
        n_stu, n_fri = map(int, input().split(' '))
        areFriends = [[False for _ in range(10)] for _ in range(10)]
        matched = [False for _ in range(10)]
        pairs = list(map(int, input().split()))
        for j in range(0,len(pairs),2):
            areFriends[pairs[j]][pairs[j+1]] = areFriends[pairs[j+1]][pairs[j]] = True
        
        result.append(countPairngs(n_stu, matched, areFriends))

    print('출력')
    for i in range(len(result)):
        print(result[i])


