"""
Author: Nguyen Tan Loc
Date: 16/10/2021
Problem:
Each image-processing function that modifies its image argument has the same
loop pattern for traversing the image. The only thing that varies is the code used
to change each pixel within the loop. Section 6.6 of this book, on higher-order
functions, suggests a simpler design pattern for such code. Design a single function, named transform, which expects an image and a function as arguments.
When this function is called, it should be passed another function that expects a
tuple of integers and returns a tuple of integers. This is the function that transforms the information for an individual pixel (such as converting it to black and
white or gray-scale). The transform function contains the loop logic for traversing its image argument. In the body of the loop, the transform function accesses
the pixel at the current position, passes it as an argument to the other function,
and resets the pixel in the image to the function’s value. Write and test a script
that defines this function and uses it to perform at least two different types of
transformation on an image.
Solution:


    ....
"""
