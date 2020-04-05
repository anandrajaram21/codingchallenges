ls = list(map(lambda x: int(x), input().split()))
c = 0
while True:
    if ls[0] > ls[1]:
        print(c)
        break
    ls[0] *= 3
    ls[1] *= 2
    c += 1

