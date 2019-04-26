import cv2 as cv
import numpy as np
import imutils
import os
import math
import inspect
import pymysql
import dataset as ds
import preProcessing as pr
import localBinaryPattern as lbp
import normalFeat as nf
import lbpFeat as lf
import classification as cl
import evaluation as ev
import PySimpleGUI as sg

def train ():
    try:
        print(" \tTraining_Analysis")

        values = []
        list = os.listdir(training_folder)
        total = len(list)
        if(total<1):
            sg.Popup('Error!','We need to get our data first!')
            print ("\nError! We need to get data first!")
            return

        trainingFeatures = [[None for x in range(total+10)] for y in range(total+10)]
        trainingClasses = [None for x in range(total+10)]

        for filename in os.listdir(training_folder):
            img = cv.imread(os.path.join(training_folder, filename), 0)
            if img is not None:
                isLBP = False
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Image file : ", filename)
                orgImg = img
                Signer = filename[:1]
                # cv.imshow(filename, img)
                orgImg , proImg = pr.preprocess(orgImg)
                # cv.imshow(filename, myImg)

                nf.normalFeat(proImg,trainingFeatures)
                lbpImg = lbp.myLbp(orgImg)
                #lbpImg = lbp.lbp(orgImg)
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

                cur.execute('''Delete FROM training_features WHERE ImageID=%s''',ImageID)
                trainfeatQuery = "INSERT INTO training_features VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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

                cur.execute('''Delete FROM training_classes WHERE ImageID=%s''',ImageID)
                trainclassQuery = "INSERT INTO training_classes VALUES (%s, %s)"
                cur.execute(trainclassQuery, values)

                if not sg.OneLineProgressMeter('Training progress', i + 1, total, 'key', orientation='h'):
                    print("Exiting Training...")
                    break

                connection.autocommit(True)

    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))
    finally:
        return

def test ():
    try:

        list = os.listdir(testing_folder)
        total = len(list)
        if(total<1):
            sg.Popup('Error!','We need to get our data first!')
            print ("\nError! We need to get data first!")
            return

        list = os.listdir(training_folder)
        total = len(list)

        trainingFeatures = [[None for x in range(total + 10)] for y in range(total + 10)]
        trainingClasses = [None for x in range(total + 10)]

        list = os.listdir(testing_folder)
        total = len(list)

        testingFeatures = [[None for x in range(total + 10)] for y in range(total + 10)]
        testingClasses = [None for x in range(total + 10)]
        decisionClasses = [None for x in range(total + 10)]
        decisions = [None for x in range(total + 10)]

        cur.execute('''SELECT * FROM training_features''')

        if (cur.rowcount == 0):
            sg.Popup('Error!','We need to train our data first!')
            print ("\nError! We need to train data first!")
            return

        i=0
        for trainfeat in cur:
            j=0
            k=1
            while(k<len(trainfeat)):
                trainingFeatures[i][j] = trainfeat[k]
                j+=1
                k+=1
            i+=1

        cur.execute('''SELECT * FROM training_classes''')
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
                Signer = filename[:1]
                # cv.imshow(filename, img)
                orgImg , proImg = pr.preprocess(orgImg)
                # cv.imshow(filename, myImg)

                nf.normalFeat(proImg,testingFeatures)
                lbpImg = lbp.myLbp(orgImg)
                #lbpImg = lbp.lbp(orgImg)
                lf.lbpFeat(lbpImg,testingFeatures)
                cl.actualclass(filename, testingClasses)
                cl.knn(trainingFeatures,testingFeatures,trainingClasses,decisionClasses,decisions,Signer)

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

                cur.execute('''Delete FROM testing_features WHERE ImageID=%s''',ImageID)
                testfeatQuery = "INSERT INTO testing_features VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                values.append(decisionClasses[i])
                values.append(decisions[i])

                cur.execute('''Delete FROM testing_classes WHERE ImageID=%s''',ImageID)
                testclassQuery = "INSERT INTO testing_classes VALUES (%s, %s, %s, %s)"
                cur.execute(testclassQuery, values)

                if not sg.OneLineProgressMeter('Testing Progress', i + 1, total, 'key', orientation='h'):
                    print("Exiting Testing...")
                    break

                connection.autocommit(True)

    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))
    finally:
        return

def testOne():

    try:
        list = os.listdir(training_folder)
        total = len(list)

        trainingFeatures = [[None for x in range(total + 10)] for y in range(total + 10)]
        trainingClasses = [None for x in range(total + 10)]

        list = os.listdir(testing_folder)
        total = len(list)

        testingFeatures = [[None for x in range(total + 10)] for y in range(total + 10)]
        testingClasses = [None for x in range(total + 10)]
        decisionClasses = [None for x in range(total + 10)]
        decisions = [None for x in range(total + 10)]

        cur.execute('''SELECT * FROM training_features''')

        if (cur.rowcount == 0):
            sg.Popup('Error!','We need to train our data first!')
            print ("\nError! We need to train data first!")
            return

        i=0
        for trainfeat in cur:
            j=0
            k=1
            while(k<len(trainfeat)):
                trainingFeatures[i][j] = trainfeat[k]
                j+=1
                k+=1
            i+=1

        cur.execute('''SELECT * FROM training_classes''')
        i = 0
        for trainclas in cur:
            trainingClasses[i] = trainclas[1]
            i += 1


        print(" \tTesting_One Image")
        values = []

        bImageFound = False

        while (not bImageFound):
            sg.ChangeLookAndFeel('SandyBeach')
            layout = [
                [sg.Text('Image Signer/Author ', size=(15, 1), auto_size_text=False, justification='left'),
                 sg.InputCombo(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'), size=(15, 1), background_color='#ffffff')],
                [sg.Text('Image Directory ', size=(15, 1), auto_size_text=False, justification='left'),
                 sg.InputText('', size=(35, 1), background_color='#ffffff'), sg.FileBrowse()],
                [sg.Submit(), sg.Cancel()]
            ]

            browser = sg.Window('Test an Image', default_element_size=(40, 1)).Layout(layout)
            button, input = browser.Read()
            if (str(button) == "Submit"):
                directory = input[1]
                signer = input[0]

                bImageFound = directory.split(".")[-1].lower() == "jpg" or directory.split(".")[-1].lower() == "png" or \
                              directory.split(".")[-1].lower() == "bmp" or directory.split(".")[-1].lower() == "jpeg"

                if (bImageFound):
                    browser.Close()
                    img = cv.imread(directory, 0)

                    if img is not None:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Directory : ", directory)
                            orgImg = img
                            cv.imshow('Original Image', img)

                            orgImg , proImg = pr.preprocess(orgImg)
                            cv.imshow('Original Image', orgImg)
                            cv.imshow('Pre-processed Image', proImg)

                            nf.normalFeat(proImg,testingFeatures)

                            lbpImg = lbp.myLbp(orgImg)
                            #lbpImg = lbp.lbp(orgImg)
                            cv.imshow('LBP Image', lbpImg)

                            lf.lbpFeat(lbpImg,testingFeatures)

                            cl.knn(trainingFeatures,testingFeatures,trainingClasses,decisionClasses,decisions,signer)

                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


                            sg.Popup('Decision : ' , decisions[0] )
                else:
                    browser.Close()
                    sg.Popup('ERROR!','Please choose an image file of type','jpg, jpeg, bmp or png')

            else:
                browser.Close()
                bImageFound=True

    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))
    finally:
        return


try:
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
      `BaselineShift` float(10,5) NOT NULL,
      `Energy` float(10,5) NOT NULL,
      `Dissimilarity` float(10,5) NOT NULL,
      `Haralick` float(10,5) NOT NULL,
      `Kurtosis` float(10,5) NOT NULL,
      `Contrast_lbp` float(10,5) NOT NULL,
      `NormalisedArea_lbp` float(10,5) NOT NULL,
      `Homogeneity_lbp` float(10,5) NOT NULL,
      `Energy_lbp` float(10,5) NOT NULL,
      `Dissimilarity_lbp` float(10,5) NOT NULL,
      `Haralick_lbp` float(10,5) NOT NULL,
      `Skewness_lbp` float(10,5) NOT NULL,
      `Kurtosis_lbp` float(10,5) NOT NULL
      )    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS `testing_features`(
      `ImageID` varchar(15) NOT NULL PRIMARY KEY,
      `AspectRatio` float(10,5) NOT NULL,
      `XCoG` float(10,5) NOT NULL,
      `YCoG` float(10,5) NOT NULL,
      `BaselineShift` float(10,5) NOT NULL,
      `Energy` float(10,5) NOT NULL,
      `Dissimilarity` float(10,5) NOT NULL,
      `Haralick` float(10,5) NOT NULL,
      `Kurtosis` float(10,5) NOT NULL,
      `Contrast_lbp` float(10,5) NOT NULL,
      `NormalisedArea_lbp` float(10,5) NOT NULL,
      `Homogeneity_lbp` float(10,5) NOT NULL,
      `Energy_lbp` float(10,5) NOT NULL,
      `Dissimilarity_lbp` float(10,5) NOT NULL,
      `Haralick_lbp` float(10,5) NOT NULL,
      `Skewness_lbp` float(10,5) NOT NULL,
      `Kurtosis_lbp` float(10,5) NOT NULL
      )    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS `training_classes`(
      `ImageID` varchar(15) NOT NULL PRIMARY KEY,
      `ActualClass` varchar(15) NOT NULL 
      )   ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS `testing_classes`(
      `ImageID` varchar(15) NOT NULL PRIMARY KEY,
      `ActualClass` varchar(15) NOT NULL ,
      `PredictionClass` varchar(15) NOT NULL,
      `Decision` varchar(15) NOT NULL
      )   ''')

    current_dir = os.path.dirname(__file__)
    training_folder = 'Data/Training'
    testing_folder = 'Data/Testing'


    sg.ChangeLookAndFeel('SandyBeach')
    layout = [
        [sg.Text('Choose what to do!', size=(15,2), font=("Helvetica", 20))],
        [sg.T(' ' * 5), sg.Button('Get Data', size=(15,2), font=("Helvetica", 15))],
        [sg.T(' ' * 5), sg.Button('Start training', size=(15,2), font=("Helvetica", 15))],
        [sg.T(' ' * 5), sg.Button('Start testing', size=(15,2), font=("Helvetica", 15))],
        [sg.T(' ' * 5), sg.Button('Start evaluating', size=(15,2), font=("Helvetica", 15))],
        [sg.T(' ' * 5), sg.Button('Test an Image', size=(15,2), font=("Helvetica", 15))],
        [sg.T(' ' * 5), sg.Button('Quit', size=(15,2), font=("Helvetica", 15))],
    ]

    button = "Start"

    while(str(button) != "Quit"):
        window = sg.Window('Signature Verifier', default_element_size=(30, 3)).Layout(layout)
        button, values = window.Read()

        if(str(button) == "Get Data"):
            window.Close()
            ds.getData()
        elif(str(button) == "Start training"):
            window.Close()
            train()
        elif(str(button) == "Start testing"):
            window.Close()
            test()
        elif(str(button) == "Start evaluating"):
            window.Close()
            ev.evaluate()
        elif(str(button) == "Test an Image"):
            window.Close()
            testOne()
        else:
            window.Close()



except Exception as error:
    print("An exception in " + inspect.stack()[0][3])
    print("Error: " + str(error))
    sg.ChangeLookAndFeel('SandyBeach')
    sg.Popup('Exception..', 'thrown in main',  str(error))






