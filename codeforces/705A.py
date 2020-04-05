n = int(input())
res = ''
for i in range(1, n+1):
    if i == n:
        if i%2 == 0:
            res += 'I love it'
            break
        else:
            res += 'I hate it'
            break
    if i%2 == 0:
        res += 'I love that '
    else:
        res += 'I hate that '
print(res)
