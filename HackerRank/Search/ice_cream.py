# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost = [[idx, val] for idx, val in enumerate(cost, 1)]
    cost.sort(key=lambda x: x[1])
    
    left = 0
    right = len(cost) - 1
    while True: 
        if cost[left][1] + cost[right][1] == money:
            break
        if cost[left][1] + cost[right][1] < money:
            left += 1
        elif cost[left][1] + cost[right][1] > money:
            right -= 1 
            
    if cost[left][0] < cost[right][0]:
        mn = cost[left][0]
        mx = cost[right][0]
    else:
        mx = cost[left][0]
        mn = cost[right][0]
    print(mn, mx)