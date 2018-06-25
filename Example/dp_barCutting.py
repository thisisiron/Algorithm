price = [0,1,5,8,8,10,18,19,20,24,29]

def cutBar(price,n):
    result = 0
    for i in range(n):
        result = max(result, price[i]+price[n-i])
    return result

print(cutBar(price, 2))
print(cutBar(price, 6))