n = int(input())
s = set(map(lambda x: int(x), input().split()))
if 1 in s:
    print('HARD')
else:
    print('EASY')
