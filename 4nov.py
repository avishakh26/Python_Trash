
import math


n,m,a = map(int, input().split())

l =math.ceil(n/a)

h =math.ceil(m/a)

k =math.ceil(l*h)

print(k)