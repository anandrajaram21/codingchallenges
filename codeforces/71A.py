n = int(input())
ls = []
for i in range(n):
    word = input()
    if len(word) <= 10:
        ls.append(word)
    else:
        new_word = word[0] + str(len(word)-2) + word[len(word)-1]
        ls.append(new_word)
for i in ls:
    print(i)
