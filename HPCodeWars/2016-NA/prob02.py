rates = []
while True:
    rate = int(input())
    if rate == 0:
        break
    rates.append(rate)
for i in rates:
    print(i, "gallons per week will last", 10000 // i, "weeks")

