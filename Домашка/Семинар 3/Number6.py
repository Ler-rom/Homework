import numpy as np
def MNK(x, y):
    l = len(x)
    k = (l*sum(x[i]*y[i] for i in range(0,l)) - sum(x)*sum(y))/ (l*sum((x[i])**2 for i in range(0,l)) - (sum(x))**2)
    b = (-sum(x)*sum(x[i]*y[i] for i in range(0,l)) + sum((x[i])**2 for i in range(0,l))*sum(y))/(l*sum((x[i])**2 for i in range(0,l)) - (sum(x))**2)
    return b, k
x = list(map(int, input().split()))
y = list(map(int, input().split()))
[B, K] = MNK(x, y)
print(B, K)





