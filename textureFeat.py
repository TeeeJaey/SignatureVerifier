import cv2 as cv
import numpy as np
import imutils
import os
import math
from scipy import ndimage
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy.stats import entropy
import mahotas as mt

def textFeat(img,featureVector):
    j=0
    i=0
    while(featureVector[i][j] is not None):
        i+=1
    i-=1
    while(featureVector[i][j] is not None):
        j+=1

    print(" \t ~~~ Texture Features ~~~")

    textures = mt.features.haralick(img)
    ht_mean = textures.mean(axis=0)
    x = 0
    ht_mean_sum = 0
    ht_mean_len = len(ht_mean)
    while (x < ht_mean_len):
        ht_mean_sum = ht_mean_sum + ht_mean[x]
        x = x + 1
    ht_mean_mean = ht_mean_sum / ht_mean_len
    print("HT_MEAN_MEAN: ", ht_mean_mean)           # Haralick Texture
    featureVector[i][j] = ht_mean_mean
    j += 1

    # ---------------------mean---------------------------------

    temp_img = img.copy()
    pixel_area = temp_img.sum()
    mean = float(pixel_area) / (img.size)
    print("Mean: ", mean)
    featureVector[i][j] = mean
    j += 1

    # -------------------variance-----------------------------------

    var_rows, var_cols = 5, 5
    var_mean = ndimage.uniform_filter(img, (var_rows, var_cols))
    var_sqr_mean = ndimage.uniform_filter(img ** 2, (var_rows, var_cols))
    variance = var_sqr_mean - var_mean ** 2
    print("Variance: ", variance)
    featureVector[i][j] = variance
    j += 1

    # --------------------skew----------------------------------

    skews = skew(img)
    y = 0
    skew_sum = 0
    skew_xlen = len(skews)
    skew_ylen = len(skews[0])
    while (y < skew_ylen):
        x = 0
        while (x < skew_xlen):
            skew_sum = skew_sum + skews[x][y]
            x += 1
        y += 1

    skew_mean = skew_sum / skews.size
    print("SKEW_MEAN: ", skew_mean)
    featureVector[i][j] = skew_mean
    j += 1

    # --------------------kurt----------------------------------

    kurt = kurtosis(img)
    y = 0
    kurt_sum = 0
    kurt_xlen = len(kurt)
    kurt_ylen = len(kurt[0])
    while (y < kurt_ylen):
        x = 0
        while (x < kurt_xlen):
            kurt_sum = kurt_sum + kurt[x][y]
            x += 1
        y += 1

    kurt_mean = kurt_sum / kurt.size
    print("KURT_MEAN: ", kurt_mean)
    featureVector[i][j] = kurt_mean
    j += 1

    # --------------------entropy----------------------------------

    entropy_img = entropy(img)
    print("KURT_MEAN: ", kurt_mean)
    featureVector[i][j] = kurt_mean
    j += 1

