import random

def count_digit(num):
    if (num//10 == 0):
        return 1
    else:
        return 1 + count_digit(num // 10)

#min , max included in random number.

def getRandomNumber(min,max):

    if min > max:
        print(" getRandomNumber(), minimum value of interval bigger than max of interval")
        return -1

    number = 0
    while number < min or number > max:
        number = 0
        exponent = 0
        minDigits = count_digit(min)
        maxDigits = count_digit(max)

        rndDigits = random.randint(minDigits,maxDigits)

        for i in range(0,rndDigits):
            digit = random.randint(0,9)
            number += digit * (10**exponent)
            exponent+=1

    return number


def driver_code():
    for attempt in range(0,0xffff):
        min = random.randint(1,99) #given by user
        max = random.randint(100,9999) #given by user
        n = getRandomNumber(min,max)
        # PRINTS RANDOM NUMBER n
        if (n >= 0):
            print(f"{min} <= {n} <= {max}")





driver_code()
