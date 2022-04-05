import math
def f(x):
    return math.atan((math.sqrt((math.pi)/3-x))/2)
x = (0+(math.pi)/3)/2
lastx = 0.0
eps = 0.0001
while abs(lastx-x) >eps:
    lastx = x
    x = f(lastx)
print(x)
