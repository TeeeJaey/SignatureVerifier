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

temp_img = [[0.0 for x in range(width)] for y in range(height)]

pixel_area = img.sum()
mean = float(pixel_area) / (img.size)
print("Mean: ", mean)

height = img.shape[0]
width = img.shape[1]

y = 0
while (y < height):
    x = 0
    while (x < width):
        temp = float(img[y][x] - mean)
        temp_img[y][x] = round(temp,2)
        x += 1
    y += 1

temp_img = np.asarray(temp_img)
variance = temp_img.sum()
print("Variance: ", variance)

