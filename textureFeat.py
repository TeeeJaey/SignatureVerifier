import cv2 as cv
import numpy as np
import imutils
import os
import math
from scipy import ndimage
from scipy import stats as scistat
import mahotas as mt
import inspect

def textFeat(img,featureVector, datafile):

    try:
        f = open("Data/"+datafile, "a")
        j=0
        i=0
        while(featureVector[i][j] is not None):
            i+=1
        i-=1
        while(featureVector[i][j] is not None):
            j+=1

        print(" \t ~~~ Texture features ~~~")
        f.write("\n ~~~ Texture features ~~~")


        # ---------------------mean---------------------------------

        temp_img = img.copy()
        pixel_area = temp_img.sum()
        mean = float(pixel_area) / (img.size)
        print("Mean: ", mean)
        f.write("\nMean: "+ str(mean))
        featureVector[i][j] = mean
        j += 1

        # -------------------variance-----------------------------------
        height = img.shape[0]
        width = img.shape[1]

        temp_img = [[0.0 for x in range(width)] for y in range(height)]
        y = 0
        while (y < height):
            x = 0
            while (x < width):
                temp = float(img[y][x] - mean)
                temp_img[y][x] = round(temp, 2)
                x += 1
            y += 1

        temp_img = np.asarray(temp_img)
        variance = temp_img.sum()
        print("Variance: ", variance)
        f.write("\nVariance: "+ str(variance))
        featureVector[i][j] = variance
        j += 1

        # --------------------skew----------------------------------

        skews = scistat.skew(img)
        skew_sum = 0
        skew_xlen = len(skews)

        x = 0
        while (x < skew_xlen):
            skew_sum = skew_sum + skews[x]
            x += 1

        skew_mean = skew_sum / skews.size
        print("Skewness: ", skew_mean)
        f.write("\nSkewness: "+ str(skew_mean))

        featureVector[i][j] = skew_mean
        j += 1

        # --------------------kurt----------------------------------

        kurt = scistat.kurtosis(img)
        kurt_sum = 0
        kurt_xlen = len(kurt)

        x = 0
        while (x < kurt_xlen):
            kurt_sum = kurt_sum + kurt[x]
            x += 1

        kurt_mean = kurt_sum / kurt.size
        print("Kurtosis: ", kurt_mean)
        f.write("\nKurtosis: "+ str(kurt_mean))

        featureVector[i][j] = kurt_mean
        j += 1

        # --------------------entropy----------------------------------

        entropy_img = scistat.entropy(img)
        entropy_len = len(entropy_img)
        x=0
        entropy_sum=0
        while (x < entropy_len):
            entropy_sum = entropy_sum + entropy_img[x]
            x += 1
        entropy_mean = entropy_sum/entropy_len

        print("Entropy: ", entropy_mean)
        f.write("\nEntropy: "+ str(entropy_mean))
        featureVector[i][j] = entropy_mean
        j += 1

        # --------------------haralick----------------------------------

        textures = mt.features.haralick(img)
        ht_mean = textures.mean(axis=0)
        x = 0
        ht_mean_sum = 0
        ht_mean_len = len(ht_mean)
        while (x < ht_mean_len):
            ht_mean_sum = ht_mean_sum + ht_mean[x]
            x = x + 1
        ht_mean_mean = ht_mean_sum / ht_mean_len
        print("Haralick: ", ht_mean_mean)           # Haralick Texture
        f.write("\nHaralick: "+ str(ht_mean_mean))
        featureVector[i][j] = ht_mean_mean
        j += 1

        print()
        f.write("\n")

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("\nError: "+ str(error))

    finally:
        f.close()
        return