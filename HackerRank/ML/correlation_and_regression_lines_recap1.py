# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

def mean(data):
    return sum(data) / len(data)

    
def var(data):
    sum_ = 0
    mean_ = mean(data)
    for d in data:
        sum_ += (d - mean_)** 2
    return sum_ 

    
def cov(data1, data2):
    sum_ = 0
    mean_d1 = mean(data1)
    mean_d2 = mean(data2)
    for i in range(len(data1)):
        sum_ += (data1[i] - mean_d1) * (data2[i] - mean_d2)
    return sum_
        

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = math.sqrt(var_physics * var_history)
print(f'{round((cov / std), 3)}'