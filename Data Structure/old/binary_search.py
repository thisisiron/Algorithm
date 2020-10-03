def binary_search(items, key):
    n = len(items)
    low = -1
    high = n

    while low + 1 < high:
        mid = int((low + high) / 2)
        if items[mid] < key:
            low = mid
        else:
            high = mid
        
    return high

x = [0,1,2,3,4,5,6,7,8,9,10]

print(binary_search(x, 9))