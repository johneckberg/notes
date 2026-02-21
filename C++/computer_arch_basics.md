# Basics of Computer Architecture:

* Von Neumann Architecture
  * main memory
  * peripherals
  * CPU (discussed cache as well)
  * secondary/disk storage
  * Connection BUS

* registers, specifically program counter
  * be able to give a high level explanation of what a register is 

* program execution cycle (fetch decode execute)

* converting decimal to binary and binary to decimal
* Decimal fractions to binary
  * use negative powers duh
  * 101011.1101 = 2^5 + 2^3 + 2^1+2^0.2^-1 + 2^-2+2^-4 = 43.8125 = 32+8+2+1+.5 +.25+.0625
* little endian vs big endian 
  * little = the least significant byte is at the lowest memory address
  * big =  the most significant byte is at the lowest memory address
* little endian is more efficient but big endian is easier to read

* sign magnitude (single bit for sign)
  * I know this isn't actually used, but would the position of the sign bit change for big endian vs little endian?
* one's compliment vs two's compliment
  * one's compliment causes the issue of having two zeros, one negative and one positive
  * ones compliment is invert, two's compliment is invert then add 1. if you get bit overflow, you disregard it 
    * this means theres only one zero! nice
  * [two's compliment works because modular arithmetic](https://math.stackexchange.com/questions/1920772/why-twos-complement-works) 
    * arithmetic modulo n is a system of addition (and subtraction) in which overflow and underflow cause you to "cycle back" to a value from 0 to n−1
    * we don't think of 11111101 as being 253 in our 8-bit system, we instead consider it to represent the number −3 (253-256). Rather than having our numbers go from 0 to 255 around a clock, we have them go from −128 to 127, where −x occupies the same spot that n−x would occupy for values of x from 1 to 128
* cpu has some register that stores overflow flag 
* range of twos compliment $\mathcal{(\text{Minimum}=-2^{n-1})}, \mathcal{(\text{Maximum}=2^{n-1}-1)}$

* recall that hexidecimal makes sense because you can more compactly represent a nibble
* base 2 is preceded 0b, hex is 0x
* Capital ASCII letters (65-90) are lower than lowercase (97-122) because the 6th bit is designed as a case-toggle, where 0 represents uppercase and 1 represents lowercase (e.g. A = $\mathcal{(65_{10}) = 0100 0001({}_{2})}$,  a = $\mathcal{(97_{10}) = 0110 0001({}_{2})}$ )