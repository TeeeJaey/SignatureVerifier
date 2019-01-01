import cv2 as cv
import imutils
import numpy as np
import math
from tkinter import *
from scipy import ndimage
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy.stats import entropy
import mahotas as mt

from skimage import feature


img = cv.imread("Obama.png")

numPoints=1
radius=1
if (len(img.shape) > 2):
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

img = imutils.resize(img, 720)
lbp = feature.local_binary_pattern(img, numPoints, radius, method="uniform")


cv.imshow('img', img)
cv.imshow('lbp', lbp)

binary = img.copy()
lbpImg = img.copy()
height = img.shape[0]
width = img.shape[1]

y = 1
while (y < height - 1):
    x = 1
    while (x < width - 1):
        binary[y - 1][x - 1] = 1 if (img[y - 1][x - 1] < img[y][x]) else 0
        binary[y - 1][x] = 1 if (img[y - 1][x] < img[y][x]) else 0
        binary[y - 1][x + 1] = 1 if (img[y - 1][x + 1] < img[y][x]) else 0

        binary[y][x - 1] = 1 if (img[y][x - 1] < img[y][x]) else 0
        binary[y][x + 1] = 1 if (img[y][x + 1] < img[y][x]) else 0

        binary[y + 1][x - 1] = 1 if (img[y + 1][x - 1] < img[y][x]) else 0
        binary[y + 1][x] = 1 if (img[y + 1][x] < img[y][x]) else 0
        binary[y + 1][x + 1] = 1 if (img[y + 1][x + 1] < img[y][x]) else 0

        lbpImg[y][x] = (binary[y][x - 1] * 128) + (binary[y - 1][x - 1] * 64) + (binary[y - 1][x] * 32) + (
                    binary[y - 1][x + 1] * 16) + (binary[y][x + 1] * 8) + (binary[y + 1][x + 1] * 4) + (
                                   binary[y + 1][x] * 2) + (binary[y + 1][x - 1] * 1)
        # lbpImg[y][x] = (binary[y-1][x+1]*128) + (binary[y][x+1]*64) + (binary[y+1][x+1]*32) + (binary[y+1][x]*16) + (binary[y+1][x-1]*8) + (binary[y][x-1]*4) + (binary[y-1][x-1]*2) + (binary[y-1][x]*1)
        x += 1
    y += 1

cv.imshow('mylbp', lbpImg)
cv.waitKey(0)
cv.destroyAllWindows()
