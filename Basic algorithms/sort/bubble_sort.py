x_list = [5,3,8,1,2,7]

for i in range(len(x_list)):
    for j in range(i+1,len(x_list)):
        if x_list[i] > x_list[j]:
            x_list[i], x_list[j] = x_list[j], x_list[i]

print(x_list)