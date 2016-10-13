from PIL import Image
import numpy as np
from tabulate import tabulate
#Number of images  (named img0, img1,... imgN)
nImages = 3
#Initial Position from Top
initialPosition = (303,733)
#Size of image to consider (pixels)
kernelSize = (2000,1500)

finalPosition = (initialPosition[0]+kernelSize[0],initialPosition[1]+kernelSize[1])
totalArea = kernelSize[0]*kernelSize[1]
totalColors = np.zeros((nImages,4))

#Load images in
im = np.empty(nImages, dtype=object)
pix= np.empty(nImages, dtype=object)
for i in range(nImages):
    im[i] = Image.open("img" + str(i) + ".JPG")
    pix[i] = im[i].load()


#Iterate through image arrays
for p in range(nImages):
    for i in range(initialPosition[0],finalPosition[0]):
        for j in range(initialPosition[1],finalPosition[1]):
                #Add each RGB value to array values
                r,g,b = pix[p][i,j]
                totalColors[p] += [0,r,g,b]

#Divide each total value by the total area of the kernel
averageColors = totalColors/totalArea

#Format and print data as n lists
for i in range(nImages):
    averageColors[i][0]=i+1

print tabulate(averageColors.tolist(),headers=["Image No.","Average R", "Average G", "Average B"])
