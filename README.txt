
					PROJECT RANDOM PLUS

                                     -------- LICENSE --------

If you want to use this idea / algorithm / software, you need to ask me first.

My email address is
<andrealbergaria@protonmail.com>
				      ------- Algorithm --------

The idea is, instead of getting a random number i get random digits, and then
use decimal number position. 

In this particular implementation , we read a byte from /dev/random, and then part it into two digits
Since a byte has 8 bits, 4 bits are the first digit, and the other 4 bits are the second digit.


Example,

Byte = 0b01010110

First Digit = 0110 (digit 6)
Second Digit = 0101 (digit 5)

So two random numbers are obtained by one byte. This improves performance (example, instead of using a byte by digit).

					------- Usage -------

Function getRandom(int numberOfDigits), returns an array of digits randomly created on heap.
After calling getRandom, programmers should use free().

After, you need to convert the array to a number. So we need to use decimal position notation.

Example :

arrayOfDigits = [3,7,1,0,2]  (called getRandom() with number of digits 5)

The array is converted to 37102 using decimal position notation
3*10^4 + 7 * 10^3 + 1 * 10^2 + 0 * 10^1 + 2*10⁰


printArray is a auxiliar function, to print the array of digits.

compile with 
	gcc randomPlus.c -g -o randomPlus

					------- Notes -------
							
Maximum digits of 64 bits (max value is 1.844674407×10¹⁹), 20 digits
Maximum digits of 32bits (max value is 4294967296), and those are 10 digits
Maximum digits for 16 bits (max value is 65536), 5 digits
Maximum digits for 8 bits (max 255), 3 digits

					------- IDEAS -------
							
Use another algorithm for getting random digits (like arc4random() or openSSL)

Port c application to python or java. Shouldnt be too dificult.



