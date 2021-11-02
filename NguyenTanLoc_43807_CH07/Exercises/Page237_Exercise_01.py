"""
Author: Nguyen Tan Loc
Date: 15/10/2021
Problem:
 Explain the advantages and disadvantages of lossless and lossy image filecompression schemes
Solution:
*Data Compression
 • After sampling an image, it can be stored in any file format. The file that contains the sampled information is known as a raw image file.
 • Though the raw image file ensures a high amount of quality, the size of the file will be too large.
 • If a file is too large then it becomes more difficult to share it over a network.
 • In this situation, compression techniques such as lossless and lossy compression come into play.
 • These are the well-known compression techniques used to reduce the size of the file.

*Lossless Compression
 • In this compression technique, the neighboring pixels of every pixel is examined. If any of the surrounding pixels
   have the same color as that of the pixel that is being examined then their positions are stored instead of storing the complete pixel.
 • In this manner, the quality of the source file remains unchanged but the size of the file is decreased.
 • Since no data of the source file is being lost, this technique is termed as lossless compression.
* Advantages:
  1. The quality of the source file is preserved.
  2. The original file can be restored from the compressed file.
* Disadvantages:
  1. The size of the file is reduced only to some extent.
  2. Though some of the data which Is not identified by the user is present in the image, it is not removed.
  3. Lossless Compression has less data holding capacity.
*Lossy Compression
 • In this compression technique, large regions of pixels are analyzed and the color values that approximate to the pixel's color is stored.
 • In this technique, the quality of the file is compromised but the size of the file is decreased to a large extent. • This technique is beneficial if the quality of the data is not the priority.
*Advantages:
  1. Some patterns of the data that are not identified by the user like rough edges are removed.
  2. The size of the file is reduced to a large extent.
  3. Lossy Compression has more data holding capacity.
*Dis-Advantages
  1. The quality of the file is compromised
  2. The exact copy of the source file cannot be restored.
    ....
"""