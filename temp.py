import cv2 as cv
import numpy as np
import math
from tkinter import *
from scipy import ndimage
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy.stats import entropy
import mahotas as mt



img = cv.imread("Obama.png")
if (len(img.shape) > 2):
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

height = img.shape[0]
width = img.shape[1]

skews = skew(img)
y = 0
skew_sum = 0
skew_xlen = len(skews)

x=0
while (x < skew_xlen):
    skew_sum = skew_sum + skews[x]
    x += 1

skew_mean = skew_sum / skews.size
print("SKEW_MEAN: ", skew_mean)




