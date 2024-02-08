
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

So two random digits are obtained by one byte. This improves performance (example, instead of using a byte by digit).
So we use decimal notation position, and have digit 1 and 5..
then by using the formula
	1 * 10^0 + 5* 10^1..than means we get 51 number.


	
			------- Python Implementation -------
			
#Auxiliary functions
count_digit(num) : returns number of digits of num. 

bytesNeeded(num) : Used to write to a random file 
("randomPython.bin", in this case is randomPython.bin
. We need to know the bytes, so to convert it to bytes object, and posteriorely write it


driverCodeRandomIntervals(): This produces min and max values, random , using  min less than max. So we get random intervals, to test for a random number between those limits. This uses 3000 attempts with random intervals, and generates random number between those intervals. Say we have min= 0xfff max =0xffff. So it will print 3000 times a random number between those.

driverCodeWriter() : same as driverCodeRandomIntervals, but it write the random numbers into a file ("randomPython.bin")
					
					------- Notes -------
							
Maximum digits of 64 bits (max value is 1.844674407×10¹⁹), 20 digits
Maximum digits of 32bits (max value is 4294967296), and those are 10 digits
Maximum digits for 16 bits (max value is 65536), 5 digits
Maximum digits for 8 bits (max 255), 3 digits

					------- IDEAS -------
							
Use another algorithm for getting random digits (like arc4random() or openSSL)


Port application to java or c. Shouldnt be too dificult.



