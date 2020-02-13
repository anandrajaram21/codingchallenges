with open('prob04-2-in.txt') as f:
    numbers = []
    results = []
    for line in f:
        numbers.append(line[:len(line)-1])
    numbers = numbers[:len(numbers)-1]
    for i in range(len(numbers)):
        numbers[i] = [float(each) for each in numbers[i].split(" ")]
    for i in numbers:
        results.append(i[0] * (10 ** i[1]))
    for i in results:
        print(round(i,2))
