"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides.
Solution:

"""
a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
if a+b>c and a+c>b and b+c>a :
      if a*a==b*b+c*c or b*b==c*c+a*a or c*c==a*a+b*b:
       loaitamgiac = 'vuông'
       print('làbacạnhcủatamgiácvuông')
else:
 print('khônglàbacạnhcủatamgiácvuông')
