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
import inspect

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

def train ():
    try:
        datafile = "Training_Analysis.txt"
        f = open("Data/"+datafile, "w")
        print(" \tTraining_Analysis")
        f.write(" \tTraining_Analysis\n")
        f.close()

        for filename in os.listdir(training_folder):
            img = cv.imread(os.path.join(training_folder, filename), 0)
            if img is not None:
                isLBP = False
                f = open("Data/" + datafile, "a")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                print("Image file : ", filename)
                f.write("\nImage file : "+ str(filename) +"\n")
                f.close()
                orgImg = img
                # cv.imshow(filename, img)
                proImg = pr.preprocess(orgImg, datafile)
                # cv.imshow(filename, myImg)

                sf.shapeFeat(proImg, trainingFeatures, isLBP, datafile)
                gf.glcm(proImg, trainingFeatures, datafile)
                tf.textFeat(proImg, trainingFeatures, datafile)

                isLBP = True
                lbpImg = lbp.lbp(orgImg, datafile)
                sf.shapeFeat(lbpImg, trainingFeatures, isLBP, datafile)
                gf.glcm(lbpImg, trainingFeatures, datafile)
                tf.textFeat(lbpImg, trainingFeatures, datafile)
                cl.actualclass(filename, trainingClasses, datafile)

                f = open("Data/" + datafile, "a")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.close()

    except Exception as error:
        f = open("Data/" + datafile, "a")
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("Error: "+ str(error))
        f.close()


def test ():
    try:
        datafile = "Testing_Analysis.txt"
        f = open("Data/"+datafile, "a")
        print(" \tTesting_Analysis")
        f.write(" \tTesting_Analysis\n\n")
        f.close()

        for filename in os.listdir(testing_folder):
            img = cv.imread(os.path.join(testing_folder, filename), 0)
            if img is not None:
                isLBP = False
                f = open("Data/" + datafile, "a")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                print("Image file : ", filename)
                f.write("\nImage file : "+ str(filename) +"\n")
                f.close()

                cl.actualclass(filename, testingClasses, datafile)
                # cv.imshow(filename, img)
                myImg = pr.preprocess(img, datafile)
                # cv.imshow(filename, myImg)

                sf.shapeFeat(myImg, trainingFeatures, isLBP, datafile)
                gf.glcm(myImg, trainingFeatures, datafile)
                tf.textFeat(myImg, trainingFeatures, datafile)

                isLBP = True
                lbpImg = lbp.lbp(myImg, datafile)
                sf.shapeFeat(lbpImg, trainingFeatures, isLBP, datafile)
                gf.glcm(lbpImg, trainingFeatures, datafile)
                tf.textFeat(lbpImg, trainingFeatures, datafile)

                cl.knn(trainingFeatures,testingFeatures,trainingClasses,decisionClasses, datafile)

                f = open("Data/" + datafile, "a")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.close()

    except Exception as error:
        f = open("Data/" + datafile, "a")
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("Error: "+ str(error))
        f.close()



current_dir = os.path.dirname(__file__)
training_folder = 'Data/Training'
testing_folder = 'Data/Testing'
temp_folder = 'TempData'

trainingFeatures = [[None for x in range(999)] for y in range(999)]
testingFeatures = [None for x in range(999)]

trainingClasses = [None for x in range(999)]
testingClasses = [None for x in range(999)]

decisionClasses = [None for x in range(999)]

askAgain=True

while(askAgain):
    inp = int(input("Choose: 1 to Start Training --- 2 to Start Testing\nChoice: "))
    if (inp == 1):
        train()
        askAgain = True
    elif (inp == 2):
        test()
        askAgain = False
    else:
        askAgain = True



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

