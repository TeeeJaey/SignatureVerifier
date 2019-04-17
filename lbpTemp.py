import cv2 as cv
import numpy as np
import imutils
import inspect
import os
import math
from matplotlib import pyplot as plt
from skimage import feature
import PySimpleGUI as sg



orgImg = cv.imread('Obama.PNG')

if (len(orgImg.shape) > 2):
    orgImg = cv.cvtColor(orgImg, cv.COLOR_RGB2GRAY)

img = imutils.resize(orgImg, 720)

height = img.shape[0]
width = img.shape[1]

numPoints = 16
radius = 2

lbp = feature.local_binary_pattern(img, numPoints, radius, method="default")

lbpImg = img.copy()
y = 1
while (y < height - 1):
    x = 1
    while (x < width - 1):
        lbpImg[y][x] = 255 - lbp[y][x]
        x += 1
    y += 1

cv.waitKey()