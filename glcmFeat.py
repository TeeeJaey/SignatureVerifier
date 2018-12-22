from skimage import feature
import numpy as np
import cv2 as cv

def glcm(img,featureVector,i):
    j=0
    while(featureVector[i][j] is not None):
        j+=1
    print(i)
    print(" \t ~~~ GLCM features~~~")

    g = feature.greycomatrix(img, [1, 5], [0, np.pi/2], levels=256, normed=True, symmetric=True)
    contrast = feature.greycoprops(g, 'contrast')
    featureVector[i][j] = contrast[0][0]
    print("Contrast: ",contrast[0][0])

    j+=1
    dissimilarity = feature.greycoprops(g, 'dissimilarity')
    featureVector[i][j] = dissimilarity[0][0]
    print("Dissimilarity: ",dissimilarity[0][0])

    j+=1
    homogeneity = feature.greycoprops(g, 'homogeneity')
    featureVector[i][j] = homogeneity[0][0]
    print("Homogeneity: ",homogeneity[0][0])

    j+=1
    energy = feature.greycoprops(g, 'energy')
    featureVector[i][j] = energy[0][0]
    print("Energy: ",energy[0][0])

    j+=1
    correlation = feature.greycoprops(g, 'correlation')
    featureVector[i][j] = correlation[0][0]
    print("Correlation: ",correlation[0][0])

    j+=1
    ASM = feature.greycoprops(g, 'ASM')
    featureVector[i][j] = ASM[0][0]
    print("ASM: ",ASM[0][0])

    return featureVector


