import cv2 as cv
import numpy as np
from tkinter import *
from scipy.stats import kurtosis
from scipy.stats import skew

img = cv.imread("Obama.png")
print("kurt : ", kurtosis(img))

skew = skew(img)
print("skew : ", skew)
y = 0
skew_sum = 0
skew_xlen = len(skew)
skew_ylen = len(skew[0])
while (y < skew_ylen):
    x = 0
    while (x < skew_xlen):
        skew_sum = skew_sum + skew[x][y]
        x += 1
    y += 1

skew_mean = skew_sum / skew.size
print("SKEW_MEAN: ", skew_mean)
"""
master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()
mainloop()

feature = [[None for x in range(99)] for y in range(99)] 
i=0
j=0
feature[0][0] = 0.334
feature[0][1] = 1928.22
feature[0][2] = 19228.22332

while(feature[i][j] is not None):
    i+=1
imageCount=i
i-=1

while(feature[i][j] is not None):
    j+=1
featureCount=j
print("Image Count: ", imageCount)
print("Feature Count: ", featureCount)
"""
