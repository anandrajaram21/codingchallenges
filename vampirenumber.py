#In number theory, a vampire number (or true vampire number) is a composite natural number with an even number of digits, that can be factored into two natural numbers each with half as many digits as the original number and not both with trailing zeroes, where the two factors contain precisely all the digits of the original number, in any order, counting multiplicity. The first vampire number is 1260 = 21 × 60.

def isPrime(n):
    if n == 1:
        return 0
    else:
        for i in range(2,n):
            if n % i == 0:
                return 0
        else:
            return 1

def numberofdigits(n):
    counter = 0
    while n != 0:
        d = n % 10
        n = n // 10
        counter += 1
    return counter

def factoring(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            for j in range(n, 0, -1):
                if n % j == 0:
                    if i * j == n:
                        if not (str(i)[-1] == '0' and str(j)[-1] == '0'):
                            factors.append((i,j))
    for i in factors:
        for j in factors:
            if j == i[::-1]:
                factors.remove(i)
    new_factors = []
    for i in factors:
        if numberofdigits(i[0]) == numberofdigits(i[1]):
            new_factors.append(i)
    return new_factors

number = int(input())
digits = []
if isPrime(number) or number < 1 or numberofdigits(number) % 2 != 0:
    print("Number doesnt meet the conditions")
else:
    factors = factoring(number)
    for i in str(number):
        digits.append(i)
    digits.sort()
    for i in factors:
        factor_string = str(i[0]) + str(i[1])
        factor_list = list(factor_string)
        factor_list.sort()
        if factor_list == digits:
            print("Vampire Number!!!")
            break
    else:
        print("Not a vampire number")
