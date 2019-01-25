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
import pymysql
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
        values = []

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

                sf.shapeFeat(proImg, trainingFeatures, isLBP, datafile, filename)
                gf.glcm(proImg, trainingFeatures, datafile)
                tf.textFeat(proImg, trainingFeatures, datafile)

                isLBP = True
                lbpImg = lbp.lbp(orgImg, datafile)
                sf.shapeFeat(lbpImg, trainingFeatures, isLBP, datafile, filename)
                gf.glcm(lbpImg, trainingFeatures, datafile)
                tf.textFeat(lbpImg, trainingFeatures, datafile)
                cl.actualclass(filename, trainingClasses, datafile)

                f = open("Data/" + datafile, "a")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                f.close()

                values.clear()
                ImageID = filename[:-4]
                values.append(ImageID)
                j = 0
                i = 0
                while (trainingFeatures[i][j] is not None):
                    i += 1
                i -= 1
                while (trainingFeatures[i][j] is not None):
                    values.append(float(trainingFeatures[i][j]))
                    j += 1

                cur.execute('''Delete FROM training_features WHERE ImageID=%s''',ImageID)
                trainfeatQuery = "INSERT INTO training_features VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(trainfeatQuery, values)

                connection.autocommit(True)

                values.clear()
                values.append(ImageID)
                j = 0
                i = 0
                while (trainingClasses[i][j] is not None):
                    i += 1
                i -= 1
                values.append(float(trainingClasses[i]))

                cur.execute('''Delete FROM training_classes WHERE ImageID=%s''',ImageID)
                trainclassQuery = "INSERT INTO training_classes VALUES (%s, %s)"
                cur.execute(trainclassQuery, values)

                connection.autocommit(True)

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
        values = []

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


                values.clear()
                ImageID = filename[:-4]
                values.append(ImageID)
                j = 0
                i = 0
                while (testingFeatures[i][j] is not None):
                    i += 1
                i -= 1
                while (testingFeatures[i][j] is not None):
                    values.append(testingFeatures[i][j])
                    j += 1

                cur.execute('''Delete FROM testing_features WHERE ImageID=%s''',ImageID)
                testfeatQuery = "INSERT INTO testing_features VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(testfeatQuery, values)

                connection.autocommit(True)

                values.clear()
                values.append(ImageID)
                j = 0
                i = 0
                while (testingClasses[i] is not None):
                    i += 1
                i -= 1
                values.append(testingClasses[i])
                i = 0
                while (decisionClasses[i] is not None):
                    i += 1
                i -= 1
                values.append(decisionClasses[i])

                cur.execute('''Delete FROM testing_classes WHERE ImageID=%s''',ImageID)
                testclassQuery = "INSERT INTO testing_classes VALUES (%s, %s, %s)"
                cur.execute(testclassQuery, values)

                connection.autocommit(True)


    except Exception as error:
        f = open("Data/" + datafile, "a")
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("Error: "+ str(error))
        f.close()



#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="signature_verifier" )
cur = connection.cursor()
# some other statements  with the help of cursor

cur.execute('''
CREATE TABLE IF NOT EXISTS `training_features` (
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `AspectRatio` float(10,5) NOT NULL,
  `XCoG` float(10,5) NOT NULL,
  `YCoG` float(10,5) NOT NULL,
  `NormalisedArea` float(10,5) NOT NULL,
  `BaselineShift` float(10,5) NOT NULL,
  `Eccentricity` float(10,5) NOT NULL,
  `HuMoments` float(10,5) NOT NULL,
  `Corners` float(10,5) NOT NULL,
  `Contrast` float(10,5) NOT NULL,
  `Dissimilarity` float(10,5) NOT NULL,
  `Homogeneity` float(10,5) NOT NULL,
  `Energy` float(10,5) NOT NULL,
  `Correlation` float(10,5) NOT NULL,
  `ASM` float(10,5) NOT NULL,
  `Mean` float(10,5) NOT NULL,
  `Variances` float(10,5) NOT NULL,
  `Skewness` float(10,5) NOT NULL,
  `Kurtosis` float(10,5) NOT NULL,
  `Entropy` float(10,5) NOT NULL,
  `Haralick` float(10,5) NOT NULL,
  `AspectRatio_lbp` float(10,5) NOT NULL,
  `XCoG_lbp` float(10,5) NOT NULL,
  `YCoG_lbp` float(10,5) NOT NULL,
  `NormalisedArea_lbp` float(10,5) NOT NULL,
  `BaselineShift_lbp` float(10,5) NOT NULL,
  `Eccentricity_lbp` float(10,5) NOT NULL,
  `HuMoments_lbp` float(10,5) NOT NULL,
  `Corners_lbp` float(10,5) NOT NULL,
  `Contrast_lbp` float(10,5) NOT NULL,
  `Dissimilarity_lbp` float(10,5) NOT NULL,
  `Homogeneity_lbp` float(10,5) NOT NULL,
  `Energy_lbp` float(10,5) NOT NULL,
  `Correlation_lbp` float(10,5) NOT NULL,
  `ASM_lbp` float(10,5) NOT NULL,
  `Mean_lbp` float(10,5) NOT NULL,
  `Variances_lbp` float(10,5) NOT NULL,
  `Skewness_lbp` float(10,5) NOT NULL,
  `Kurtosis_lbp` float(10,5) NOT NULL,
  `Entropy_lbp` float(10,5) NOT NULL,
  `Haralick_lbp` float(10,5) NOT NULL
  )    ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS `testing_features`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `AspectRatio` float(10,5) NOT NULL,
  `XCoG` float(10,5) NOT NULL,
  `YCoG` float(10,5) NOT NULL,
  `NormalisedArea` float(10,5) NOT NULL,
  `BaselineShift` float(10,5) NOT NULL,
  `Eccentricity` float(10,5) NOT NULL,
  `HuMoments` float(10,5) NOT NULL,
  `Corners` float(10,5) NOT NULL,
  `Contrast` float(10,5) NOT NULL,
  `Dissimilarity` float(10,5) NOT NULL,
  `Homogeneity` float(10,5) NOT NULL,
  `Energy` float(10,5) NOT NULL,
  `Correlation` float(10,5) NOT NULL,
  `ASM` float(10,5) NOT NULL,
  `Mean` float(10,5) NOT NULL,
  `Variances` float(10,5) NOT NULL,
  `Skewness` float(10,5) NOT NULL,
  `Kurtosis` float(10,5) NOT NULL,
  `Entropy` float(10,5) NOT NULL,
  `Haralick` float(10,5) NOT NULL,
  `AspectRatio_lbp` float(10,5) NOT NULL,
  `XCoG_lbp` float(10,5) NOT NULL,
  `YCoG_lbp` float(10,5) NOT NULL,
  `NormalisedArea_lbp` float(10,5) NOT NULL,
  `BaselineShift_lbp` float(10,5) NOT NULL,
  `Eccentricity_lbp` float(10,5) NOT NULL,
  `HuMoments_lbp` float(10,5) NOT NULL,
  `Corners_lbp` float(10,5) NOT NULL,
  `Contrast_lbp` float(10,5) NOT NULL,
  `Dissimilarity_lbp` float(10,5) NOT NULL,
  `Homogeneity_lbp` float(10,5) NOT NULL,
  `Energy_lbp` float(10,5) NOT NULL,
  `Correlation_lbp` float(10,5) NOT NULL,
  `ASM_lbp` float(10,5) NOT NULL,
  `Mean_lbp` float(10,5) NOT NULL,
  `Variances_lbp` float(10,5) NOT NULL,
  `Skewness_lbp` float(10,5) NOT NULL,
  `Kurtosis_lbp` float(10,5) NOT NULL,
  `Entropy_lbp` float(10,5) NOT NULL,
  `Haralick_lbp` float(10,5) NOT NULL
  )    ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS `training_classes`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `ActualClass` varchar(15) NOT NULL 
  )   ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS `testing_classes`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `DecisionClass` varchar(15) NOT NULL,
  `ActualClass` varchar(15) NOT NULL 
  )   ''')

current_dir = os.path.dirname(__file__)
training_folder = 'Data/Training'
testing_folder = 'Data/Testing'
temp_folder = 'TempData'

trainingFeatures = [[None for x in range(999)] for y in range(999)]
testingFeatures = [[None for x in range(999)] for y in range(999)]
trainingClasses = [None for x in range(999)]
testingClasses = [None for x in range(999)]
decisionClasses = [None for x in range(999)]

askAgain=True
while(askAgain):
    inp = int(input("1 to Start Training \n2 to Start Testing\n3 to Exit\nChoice: "))
    if (inp == 1):
        train()
    elif (inp == 2):
        test()
    elif (inp == 3):
        print("Good Bye!")
        askAgain = False
    else:
        print("Invalid input!")


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

