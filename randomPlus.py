#
# Ways to measure entropy in linux
# Ent tool , you can find in the below site
#   https://www.fourmilab.ch/random/
# usage : cat 1-gb-file.img | ent

# Or binwalk ...i only tested ent.
# binwalk -E file


from random import *
from math import log
import sys



def count_digit(num):
    if (num//10 == 0):
        return 1
    else:
        return 1 + count_digit(num // 10)


#auxiliary function, to convert a list of digits (got by getRandomNumber(min,max), and convert to a number
# using decimal position notation.
def convertListOfDigitsIntoNumber(lstDigits):
    exponent = 0
    number = 0

    for digit in lstDigits:
        number += digit * (10**exponent)
        exponent += 1

    return number

# This function returns a random between min and max
# If it fails, it will return -1
def getRandomNumber(min,max):


    exponent = 0
    number = 0
    if min > max:
        print("min cant be bigger than max..returning")
        return

    digitCountMin = count_digit(min)
    digitCountMax = count_digit(max)
    # If digitCountMin == digitCountMax ,no need to check
    # it will return digitCountMin(which is equal to digitCountMax)
    #numberOfDigits = randint(digitCountMin,digitCountMax)
    numberOfDigits = digitCountMax
    digitsInList = []
    if numberOfDigits == 1:
        number = randint(min,max)
    else:
        for currentDigit in range(0,numberOfDigits):

            curDigit = getrandbits(4)

            if curDigit >= 10:
                curDigit = curDigit - 10

            digitsInList.append(curDigit)

        number = convertListOfDigitsIntoNumber(digitsInList)
        if number > max or number < min:
            return -1

        return number


#Found on www.
# Bytes needed for a number to write to file

def bytesNeeded(n):
    if n == 0:
        return 1
    return int(log(n, 256)) + 1

#
# Justs uses random intervals, and calculate the random in between those intervals
# Justs prints values to output.
#
def driverCodeRandomIntervals():
    for attempts in range(0,3000):
        min = randint(1,8000)
        max = randint(8000,9000)
        n = getRandomNumber(min,max)
        while (n == -1):
            n = getRandomNumber(min,max)
        print(f" random number : {n}, between [{min},{max}]")
#
# Writes all the random values to randomPython.bin file.
#

def driverCodeWrite():
    file_path = "randomPython.bin"
    with open(file_path, "wb") as file:
        for attempts in range(0,90000):
            min = 0xfffffffffffffff
            max = 0xfffffffffffff

            rndNumber = getRandomNumber(min,max)
            while (rndNumber == -1):
                rndNumber = getRandomNumber(min,max)

            #DEBUG
            #print(f" random number : {rndNumber}, between [{min},{max}]")
            #END DEBUG

            #Write to file
            lenRandomObject = bytesNeeded(rndNumber)
            rndObject = rndNumber.to_bytes(lenRandomObject,"little")
            file.write(rndObject)

driverCodeWrite()






