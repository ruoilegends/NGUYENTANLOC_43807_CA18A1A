"""
Author: Nguyen Tan Loc
Date: 24/09/2021
Problem:
   Consult the Table of ASCII values in Chapter 2 and suggest how you would modify
the encryption and decryption scripts in this section to work with strings containing all of the printable characters.
Solution:
• ASCII stands for American Standard code for Information interchange.
• This is a character coding standard that represents both printable and non-printable characters.
• ASCII can represent a total of 128 characters out of which 95 are printable and the remaining 33 characters are non-printable characters.
• Printable characters include digits from 0 to 9, upper case letters A to Z, lower case letters a to z and punctuation symbols.
• The range of printable characters in ASCII is from 32(space) to 126(z).
 • We can find the code that encrypts the given string with a given distance in the text book itself but it can encrypt only the string that contains lower case letters.
 • To modify the encryption and decryption scripts change the character 'a' in the code to character (space) this is so because the printable characters range starts form space(32) and the last character is 'Z' itself.
 • The modifications that are made are highlighted with yellow color.
    ....
"""