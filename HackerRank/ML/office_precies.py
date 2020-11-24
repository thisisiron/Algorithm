# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np
import sys
input = sys.stdin.readline

F, N = map(int, input().split())

X, Y = [], []
for _ in range(N):
    data = list(map(float, input().split()))
    X.append(data[:F])
    Y.append(data[F])
    
poly = PolynomialFeatures(3, include_bias=False)
model = linear_model.LinearRegression()
model.fit(poly.fit_transform(np.array(X)), Y)

T = int(input())
X_test = []
for _ in range(T):
    X_test.append(list(map(float, input().split())))
answer = model.predict(poly.fit_transform(np.array(X_test)))
    
for ans in answer:
    print(ans, sep="\n")