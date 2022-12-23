# pi**2/6 = 1 + 1/4 * 1/9 ...

import math

i = 1
j = -1
p1 = 0
p2 = 1

while i < 1000:
    p1 = p1 + 1/i**2
    p2 = p2 + j**i * 1/(1+2*i)
    i = i + 1

pi1 = math.sqrt(p1*6)
pi2 = 4*p2

print("iter, pi est, err")
print(i, pi1, math.pi - pi1)
print(i, pi2, math.pi - pi2)