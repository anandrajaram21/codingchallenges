n = int(input())
c = 0
for i in range(n):
    k = list(map(lambda x: int(x), input().split()))
    if k.count(1) >= 2:
        c+= 1
print(c)
