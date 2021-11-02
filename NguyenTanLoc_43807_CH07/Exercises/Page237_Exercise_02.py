"""
Author: Nguyen Tan Loc
Date: 15/10/2021
Problem:
The size of an image is 1680 pixels by 1050 pixels. Assume that this image has been
sampled using the RGB color system and placed into a raw image file. What is the
minimum size of this file in megabytes? (Hint: There are 8 bits in a byte, 1024 bits in
a kilobyte, and 1000 kilobytes in a megabyte.)
Solution:
•A Pixel is the fundamental unit of an image.
• An image is composed of millions of pixels arranged together in rows and columns.
• Each pixel represents a color. If the image is black and white then the total possible colors are black and white.
  To store two different colors, we need one bit. Hence, in a black and white picture, each pixel is equal to one bit.
• If the image is a colored picture then the color of the pixel is represented in the form of RGB. To represent a color
  in RGB we require 24 bits. 8 bits are required to representèach consistent color. Hence, if the image is colored then
  each pixel in the picture is equal to 24 bits
    ....
"""