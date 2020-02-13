with open('prob03-2-in.txt') as f:
    words = []
    lines = f.readlines()
    for i in range(1, len(lines)):
        if i == len(lines) - 1:
            words.append(lines[i])
            break
        words.append(lines[i][:len(lines[i])-1])
    print(words)
    for i in words:
        for letter in range(len(i)-1):
            if i[letter] == i[letter+1]:
                print("likes",i)
                break
        else:
            print("hates",i)
