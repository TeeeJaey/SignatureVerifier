import cv2 as cv
import numpy as np
import imutils
import os
import math
import preProcessing as pr
import localBinaryPattern as lbp
import shapeFeat as sf
import glcmFeat as gf
import textureFeat as tf
import classification as cl

"""
print("~~~~~~~~ Ob Img ~~~~~~~~~~~")
obImg = cv.imread("Obama.png")
cv.imshow("obImg",obImg)
obImg = pp.preprocess(obImg)
cv.imshow("obFinal", obImg)
#sf.features(obImg)
#gc.glcm(obImg)

print("~~~~~~~~ My Img ~~~~~~~~~~~")    
myImg = cv.imread("mySign.jpeg")
cv.imshow("myImg",myImg)
myImg = pp.preprocess(myImg)
cv.imshow("myFinal", myImg)
#sf.features(myImg)
#gc.glcm(myImg)
"""

current_dir = os.path.dirname(__file__)
training_folder = 'Data/Training'
testing_folder = 'Data/Testing'
temp_folder = 'TempData'

trainingFeatures = [[None for x in range(999)] for y in range(999)]
testingFeatures = [None for x in range(999)]
trainingClasses = [None for x in range(999)]
testingClasses = [None for x in range(999)]

for filename in os.listdir(training_folder):
    img = cv.imread(os.path.join(training_folder, filename), 0)
    if img is not None:
        isLBP = False
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Image file : ",filename)
        orgImg = img
        #cv.imshow(filename, img)
        proImg = pr.preprocess(orgImg)
        #cv.imshow(filename, myImg)

        sf.shapeFeat(proImg,trainingFeatures,isLBP)
        gf.glcm(proImg,trainingFeatures)
        tf.textFeat(proImg,trainingFeatures)

        isLBP = True
        lbpImg = lbp.lbp(orgImg)
        sf.shapeFeat(lbpImg,trainingFeatures,isLBP)
        gf.glcm(lbpImg,trainingFeatures)
        tf.textFeat(lbpImg,trainingFeatures)
        cl.actualclass(filename, trainingClasses)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

inp = input("Type 'start test' to start test..")
if(inp == "start test"):

    for filename in os.listdir(testing_folder):
        img = cv.imread(os.path.join(testing_folder, filename), 0)
        if img is not None:
            isLBP = False
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Image file : ",filename)
            cl.actualclass(filename, testingClasses)
            # cv.imshow(filename, img)
            myImg = pr.preprocess(img)
            # cv.imshow(filename, myImg)

            sf.shapeFeat(myImg, trainingFeatures, isLBP)
            gf.glcm(myImg, trainingFeatures)
            tf.textFeat(myImg, trainingFeatures)

            isLBP = True
            lbp.lbp(myImg)
            sf.shapeFeat(myImg, trainingFeatures, isLBP)
            gf.glcm(myImg, trainingFeatures)
            tf.textFeat(myImg, trainingFeatures)

            decision  = cl.knn(myImg,trainingFeatures,trainingClasses)
            print("Decision Class : ",decision)

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

"""
i=0
j=0
while(trainingFeatures[i][j] is not None):
    while(trainingFeatures[i][j] is not None):
        print (trainingFeatures[i][j],end=", ")
        j+=1
    print ()
    j=0
    i+=1
cv.waitKey(0)
cv.destroyAllWindows()

"""

