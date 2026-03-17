
n, m, k = map(int, input().split())


x = min(n, m, k)

n -= x
m -= x
k -= x

y = min(n // 2, k)

print(x + y)


