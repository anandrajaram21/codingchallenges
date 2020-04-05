ls = list(map(lambda x: int(x), input().split()))
arr = list(input())
n = ls[0]
t = ls[1]
c = 0
res = []
for i in range(t):
    for j in range(len(arr)-1):
        p1 = arr[j]
        p2 = arr[j+1]
        if p1 < p2:
            res.append(p2)
            res.append(p1)
        else:
            res.append(p1)
res = ''.join(res)
print(res)
