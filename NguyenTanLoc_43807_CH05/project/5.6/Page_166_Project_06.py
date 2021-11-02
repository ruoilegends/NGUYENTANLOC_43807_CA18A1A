"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases
Solution:

    ....
"""
def decimalToRep(num,base1):
    base = ""
    while num > 0:
        one = int(num % base1)
        if one < 10:
            base += str(one)
        else:
            base += chr(ord('A')+one-10)
        num //= base1
    base = base[::-1]
    return base
def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

if __name__ == "__main__":
    main()