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


def normalFeat(img,featureVector):

    try:
       #f= open("Data/"+datafile, "a")
        j=0
        i=0
        while(featureVector[i][j] is not None):
            i+=1
        while(featureVector[i][j] is not None):
            j+=1

        print(" \t ~~~ Normal features ~~~")
       #f.write("\n ~~~ Normal features ~~~")


        height = img.shape[0]
        width = img.shape[1]


        # -------------------------Aspect Ratio-----------------------------

        aspectratio = float(img.shape[1]/img.shape[0])
        print("Aspect Ratio : ",aspectratio)
       #f.write("\nAspect Ratio: "+ str(aspectratio))
        featureVector[i][j] = aspectratio
        j+=1

        # -------------------------X_COG-----------------------------

        Y_coord , X_coord = img.nonzero()
        X_COG = X_coord.sum()/X_coord.size
        Y_COG = Y_coord.sum()/Y_coord.size
        print("X_COG: "+ str(X_COG))
       #f.write("\nX_COG: "+ str(X_COG))
        featureVector[i][j] = X_COG
        j+=1

        # -------------------------Y_COG-----------------------------

        print("Y_COG: "+ str(Y_COG))
       #f.write("\nY_COG: "+ str(Y_COG))
        featureVector[i][j] = Y_COG
        j+=1


        # -------------------------Baseline shift-----------------------------

        left_ = img[:,0:int(X_COG)]
        left_Y_COG , _ = left_.nonzero()
        left_Y_COG = left_Y_COG.sum()/left_Y_COG.size

        right_ = img[:,int(X_COG):]
        right_Y_COG , _ = right_.nonzero()
        right_Y_COG = right_Y_COG.sum()/right_Y_COG.size

        baseline_shift = abs(right_Y_COG - left_Y_COG)
        print("Baseline shift: ",baseline_shift)
       #f.write("\nBaseline shift: "+ str(baseline_shift))
        featureVector[i][j] = baseline_shift
        j+=1

        g = feature.greycomatrix(img, [1, 5], [0, np.pi/2], levels=256, normed=True, symmetric=True)



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
