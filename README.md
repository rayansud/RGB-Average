# RGB-Average

Average out the RGB values in a set of images, over a specified kernel size

The images should be of the same size.



**Usage:**

1. Download the main.py file

2. Place all the images you want to analyze in the same folder as main.py, named "img0.JPG", "img1.JPG", etc. and specify the number of images in the variable nImages

3. Specify the initial position on the images - (0,0) = top corner, (max_width,max_height) = bottom corner - in the variable initialPosition

4. Specify the size to analyse in the variable kernelSize

5. Run the script!

*I created this utility to analyze experimental data from a photoelasticity experiment. A plastic was subjected to increasing amounts of stress, and photographed through a polarizer setup. A central kernel area was iterated over, the average RGB values were found, and plotted against stress in the plastic.*
