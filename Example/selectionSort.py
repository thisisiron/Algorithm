x_list = [5,3,8,1,2,7]

for i in range(len(x_list)):
    max_num = i
    for j in range(i+1,len(x_list)):
        if x_list[j] > x_list[max_num]:
            max_num = j
    x_list[i], x_list[max_num] = x_list[max_num], x_list[i]
    print(i, max_num, x_list)
print(x_list)
# i j
# 0 2 [8, 3, 5, 1, 2, 7]
# 1 5 [8, 7, 5, 1, 2, 3]
# 2 2 [8, 7, 5, 1, 2, 3]
# 3 5 [8, 7, 5, 3, 2, 1]
# 4 4 [8, 7, 5, 3, 2, 1]
# 5 5 [8, 7, 5, 3, 2, 1]