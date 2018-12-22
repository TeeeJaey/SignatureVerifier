import cv2 as cv
import numpy as np
import imutils
import math


def shapeFeat(img,featureVector, isLBP):
    j=0
    i=0
    while(featureVector[i][j] is not None):
        i+=1
    if(isLBP):
        i-=1
    while(featureVector[i][j] is not None):
        j+=1
        
    print(" \t ~~~ Shape Features ~~~")
    print("Img_dim: ",img.shape)

    # -------------------------Aspect Ratio-----------------------------
    # Aspect ratio
    aspectratio = float(img.shape[1]/img.shape[0])
    print("Aspect Ratio : ",aspectratio)
    featureVector[i][j] = aspectratio
    j+=1

    # ------------------------Centre of Gravity------------------------------

    Y_coord , X_coord = img.nonzero()
    X_COG = X_coord.sum()/X_coord.size
    Y_COG = Y_coord.sum()/Y_coord.size
    print("Centre of Gravity : (",X_COG,",",Y_COG,")")
    featureVector[i][j] = X_COG
    j+=1
    featureVector[i][j] = Y_COG
    j+=1

    # ------------------------Normalized area------------------------------

    temp_img = img.copy()
    temp_img[temp_img == 255] = 1    
    pixel_area = temp_img.sum()
    normalised_area = float(pixel_area)/(img.size)
    print("Normalized area: ",normalised_area)
    featureVector[i][j] = normalised_area
    j+=1


    # -------------------------Baseline shift-----------------------------

    left_ = img[:,0:int(X_COG)]
    left_Y_COG , _ = left_.nonzero()
    left_Y_COG = left_Y_COG.sum()/left_Y_COG.size

    right_ = img[:,int(X_COG):]
    right_Y_COG , _ = right_.nonzero()
    right_Y_COG = right_Y_COG.sum()/right_Y_COG.size

    baseline_shift = abs(right_Y_COG - left_Y_COG)
    print("Baseline shift : ",baseline_shift)
    featureVector[i][j] = baseline_shift

    print()
