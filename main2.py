import cv2 as cv
import numpy as np
import imutils
import os
import math
import inspect
import pymysql
import preProcessing as pr
import localBinaryPattern as lbp
import normalFeat as nf
import lbpFeat as lf
import classification as cl


def train ():
    try:
        print(" \tTraining_Analysis")
        values = []

        for filename in os.listdir(training_folder):
            img = cv.imread(os.path.join(training_folder, filename), 0)
            if img is not None:
                isLBP = False
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Image file : ", filename)
                orgImg = img
                # cv.imshow(filename, img)
                proImg = pr.preprocess(orgImg)
                # cv.imshow(filename, myImg)

                nf.normalFeat(proImg,trainingFeatures)
                lbpImg = lbp.lbp(orgImg)
                lf.lbpFeat(lbpImg,trainingFeatures)
                cl.actualclass(filename, trainingClasses)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

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

                cur.execute('''Delete FROM training_features2 WHERE ImageID=%s''',ImageID)
                trainfeatQuery = "INSERT INTO training_features2 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(trainfeatQuery, values)

                connection.autocommit(True)

                values.clear()
                values.append(ImageID)
                j = 0
                i = 0
                while (trainingClasses[i] is not None):
                    i += 1
                i -= 1
                values.append(trainingClasses[i])

                cur.execute('''Delete FROM training_classes2 WHERE ImageID=%s''',ImageID)
                trainclassQuery = "INSERT INTO training_classes2 VALUES (%s, %s)"
                cur.execute(trainclassQuery, values)

                connection.autocommit(True)

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))

def test ():
    try:

        trainingFeatures = [[None for x in range(999)] for y in range(999)]
        cur.execute('''SELECT * FROM training_features2''')
        i=0
        for trainfeat in cur:
            j=0
            k=1
            while(k<len(trainfeat)):
                trainingFeatures[i][j] = trainfeat[k]
                j+=1
                k+=1
            i+=1

        trainingClasses = [None for x in range(999)]
        cur.execute('''SELECT * FROM training_classes2''')
        i = 0
        for trainclas in cur:
            trainingClasses[i] = trainclas[1]
            i += 1


        print(" \tTesting_Analysis")
        values = []

        for filename in os.listdir(testing_folder):
            img = cv.imread(os.path.join(testing_folder, filename), 0)
            if img is not None:
                isLBP = False
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Image file : ", filename)
                orgImg = img
                # cv.imshow(filename, img)
                proImg = pr.preprocess(orgImg)
                # cv.imshow(filename, myImg)

                nf.normalFeat(proImg,testingFeatures)
                lbpImg = lbp.lbp(orgImg)
                lf.lbpFeat(lbpImg,testingFeatures)
                cl.actualclass(filename, testingClasses)
                cl.knn(trainingFeatures,testingFeatures,trainingClasses,decisionClasses,  filename)

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                values.clear()
                ImageID = filename[:-4]
                values.append(ImageID)
                j = 0
                i = 0
                while (testingFeatures[i][j] is not None):
                    i += 1
                i -= 1
                while (testingFeatures[i][j] is not None):
                    values.append(float(testingFeatures[i][j]))
                    j += 1

                cur.execute('''Delete FROM testing_features2 WHERE ImageID=%s''',ImageID)
                testfeatQuery = "INSERT INTO testing_features2 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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

                cur.execute('''Delete FROM testing_classes2 WHERE ImageID=%s''',ImageID)
                testclassQuery = "INSERT INTO testing_classes2 VALUES (%s, %s, %s)"
                cur.execute(testclassQuery, values)

                connection.autocommit(True)


    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="signature_verifier" )
cur = connection.cursor()
# some other statements  with the help of cursor


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



