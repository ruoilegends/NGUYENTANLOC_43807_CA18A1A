"""
Author: Nguyen Tan Loc
Date: 10/09/2021
Problem: Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.
Solution:

"""
a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
if a+b>c and a+c>b and b+c>a :
      if a==b and b==c:
       loaitamgiac = 'đều'
       print('làbacạnhcủatamgiácđều')
else:
 print('khônglàbacạnhcủatamgiácđều')








