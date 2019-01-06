from skimage import feature
import numpy as np
import cv2 as cv
import inspect

def glcm(img,featureVector, datafile):

    try:
        f = open("Data/"+datafile, "a")
        j=0
        i=0
        while(featureVector[i][j] is not None):
            i+=1
        i-=1
        while(featureVector[i][j] is not None):
            j+=1

        print(" \t ~~~ GLCM features ~~~")
        f.write("\n ~~~ GLCM features ~~~")

        g = feature.greycomatrix(img, [1, 5], [0, np.pi/2], levels=256, normed=True, symmetric=True)
        contrast = feature.greycoprops(g, 'contrast')
        featureVector[i][j] = contrast[0][0]
        print("Contrast: ",contrast[0][0])
        f.write("\nContrast: "+ str(contrast[0][0]))

        j+=1
        dissimilarity = feature.greycoprops(g, 'dissimilarity')
        featureVector[i][j] = dissimilarity[0][0]
        print("Dissimilarity: ",dissimilarity[0][0])
        f.write("\nDissimilarity: "+ str(dissimilarity[0][0]))

        j+=1
        homogeneity = feature.greycoprops(g, 'homogeneity')
        featureVector[i][j] = homogeneity[0][0]
        print("Homogeneity: ",homogeneity[0][0])
        f.write("\nHomogeneity: "+ str(homogeneity[0][0]))

        j+=1
        energy = feature.greycoprops(g, 'energy')
        featureVector[i][j] = energy[0][0]
        print("Energy: ",energy[0][0])
        f.write("\nEnergy: "+ str(energy[0][0]))

        j+=1
        correlation = feature.greycoprops(g, 'correlation')
        featureVector[i][j] = correlation[0][0]
        print("Correlation: ",correlation[0][0])
        f.write("\nCorrelation: "+ str(correlation[0][0]))

        j+=1
        ASM = feature.greycoprops(g, 'ASM')
        featureVector[i][j] = ASM[0][0]
        print("ASM: ",ASM[0][0])
        f.write("\nASM: "+ str(ASM[0][0]))

        print()
        f.write("\n")

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("\nError: "+ str(error))

    finally:
        f.close()
        return