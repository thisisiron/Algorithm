x_list = [5,3,8,1,2,7]

for i in range(1, len(x_list)):
    key = x_list[i]
    j = i-1
    while j>=0 and x_list[j] > key:
        x_list[j+1] = x_list[j]
        j -= 1
    x_list[j+1] = key
    print(x_list)
    

print(x_list)
# [5, 3, 8, 1, 2, 7]
# 3 선택
# [3, 5, 8, 1, 2, 7]
# 8 선택
# [3, 5, 8, 1, 2, 7]
# 1 선택
# [1, 3, 5, 8, 2, 7]
# 2 선택
# [1, 2, 3, 5, 8, 7]
# 7 선택
# [1, 2, 3, 5, 7, 8]
# [1, 2, 3, 5, 7, 8]
print('--------------------------------')

def insertion_sort(items):
    for i in range(len(items)):
        j = i
        while j > 0 and items[j - 1] > items[i]:
            items[j-1], items[i] = items[i], items[j-1]
            j-=1
    return items

print(insertion_sort(x_list))