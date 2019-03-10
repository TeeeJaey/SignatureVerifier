import cv2 as cv
import numpy as np
import imutils
import math
import inspect
from scipy import stats as scistat
import mahotas as mt
from skimage import measure
from skimage import feature
import PySimpleGUI as sg


def lbpFeat(img,featureVector):

    try:

        j=0
        i=0
        while(featureVector[i][j] is not None):
            i+=1
        i-=1
        while(featureVector[i][j] is not None):
            j+=1

        print(" \t ~~~ LBP features ~~~")
        # f.write("\n ~~~ LBP features ~~~")
        # ------------------------Contrast------------------------------

        g = feature.greycomatrix(img, [1, 5], [0, np.pi/2], levels=256, normed=True, symmetric=True)
        contrast = feature.greycoprops(g, 'contrast')
        featureVector[i][j] = contrast[0][0]
        print("Contrast: ",contrast[0][0])
       #f.write("\nContrast: "+ str(contrast[0][0]))
        j+=1


        # ------------------------Normalized area------------------------------

        temp_img = img.copy()
        temp_img[temp_img > 180] = 1
        pixel_area = temp_img.sum()
        normalised_area = float(pixel_area)/(img.size)
        print("Normalized area: ",normalised_area)
       #f.write("\nNormalized area: "+ str(normalised_area))
        featureVector[i][j] = normalised_area
        j+=1

        # ------------------------Homogeneity------------------------------

        homogeneity = feature.greycoprops(g, 'homogeneity')
        featureVector[i][j] = homogeneity[0][0]
        print("Homogeneity: ",homogeneity[0][0])
       #f.write("\nHomogeneity: "+ str(homogeneity[0][0]))
        j+=1

        # --------------------Energy----------------------------------

        energy = feature.greycoprops(g, 'energy')
        featureVector[i][j] = energy[0][0]
        print("Energy: ",energy[0][0])
       #f.write("\nEnergy: "+ str(energy[0][0]))
        j+=1

        # --------------------Dissimilarity----------------------------------

        dissimilarity = feature.greycoprops(g, 'dissimilarity')
        print("Dissimilarity: ",dissimilarity[0][0])
       #f.write("\nDissimilarity: "+ str(dissimilarity[0][0]))
        featureVector[i][j] = dissimilarity[0][0]
        j+=1


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
       #f.write("\nHaralick: "+ str(ht_mean_mean))
        featureVector[i][j] = ht_mean_mean
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
       #f.write("\nSkewness: "+ str(skew_mean))

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
       #f.write("\nKurtosis: "+ str(kurt_mean))

        featureVector[i][j] = kurt_mean
        j += 1

        print()
       #f.write("\n")


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))

    finally:
       #f.close()
        return