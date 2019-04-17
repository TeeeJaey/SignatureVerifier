import cv2 as cv
import numpy as np
import imutils
import inspect
import os
import math
from matplotlib import pyplot as plt
from skimage import feature
import PySimpleGUI as sg


def lbp(img):
    try:
        # f = open("Data/"+datafile, "a")

        height = img.shape[0]
        width = img.shape[1]

        numPoints = 32  # 16
        radius = 4  # 2

        lbp = feature.local_binary_pattern(img, numPoints, radius, method="default")

        lbpImg = img.copy()
        y = 1
        while (y < height - 1):
            x = 1
            while (x < width - 1):
                lbpImg[y][x] = 255 - lbp[y][x]
                x += 1
            y += 1


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: " + str(error))
        sg.ChangeLookAndFeel('SandyBeach')
        sg.Popup('Exception..', 'thrown in ', str(inspect.stack()[0][3]), str(error))


    finally:
        # f.close()
        return lbpImg


def myLbp(img):
    try:
        height = img.shape[0]
        width = img.shape[1]

        binary = img.copy()
        lbpImg = img.copy()

        y = 1
        while (y < height - 1):
            x = 1
            while (x < width - 1):
                binary[y - 1][x - 1] = 1 if (img[y - 1][x - 1] < img[y][x]) else 0
                binary[y - 1][x] = 1 if (img[y - 1][x] < img[y][x]) else 0
                binary[y - 1][x + 1] = 1 if (img[y - 1][x + 1] < img[y][x]) else 0

                binary[y][x - 1] = 1 if (img[y][x - 1] < img[y][x]) else 0
                binary[y][x + 1] = 1 if (img[y][x + 1] < img[y][x]) else 0

                binary[y + 1][x - 1] = 1 if (img[y + 1][x - 1] < img[y][x]) else 0
                binary[y + 1][x] = 1 if (img[y + 1][x] < img[y][x]) else 0
                binary[y + 1][x + 1] = 1 if (img[y + 1][x + 1] < img[y][x]) else 0

                """
                # ```````````````  anti Clockwise   ```````````
                # r     81.92
                lbpImg[y][x] = (binary[y][x + 1] * 128) + (binary[y - 1][x + 1] * 64) + (binary[y - 1][x] * 32) + (
                        binary[y - 1][x - 1] * 16) + (binary[y][x - 1] * 8) + (binary[y + 1][x - 1] * 4) + (
                                       binary[y + 1][x] * 2) + (binary[y + 1][x + 1] * 1)
                


                # br    82.31
                lbpImg[y][x] = (binary[y + 1][x + 1] * 128) + (binary[y][x + 1] * 64) + (binary[y - 1][x + 1] * 32) + (
                        binary[y - 1][x] * 16) + (binary[y - 1][x - 1] * 8) + (binary[y][x - 1] * 4) + (
                                       binary[y + 1][x - 1] * 2) + (binary[y + 1][x] * 1)

                


                # b     81.92
                lbpImg[y][x] = (binary[y + 1][x] * 128) + (binary[y + 1][x + 1] * 64) + (binary[y][x + 1] * 32) + (
                        binary[y - 1][x + 1] * 16) + (binary[y - 1][x] * 8) + (binary[y - 1][x - 1] * 4) + (
                                       binary[y][x - 1] * 2) + (binary[y + 1][x - 1] * 1)

                # bL    81.54
                lbpImg[y][x] = (binary[y + 1][x - 1] * 128) + (binary[y + 1][x] * 64) + (binary[y + 1][x + 1] * 32) + (
                        binary[y][x + 1] * 16) + (binary[y - 1][x + 1] * 8) + (binary[y - 1][x] * 4) + (
                                       binary[y - 1][x - 1] * 2) + (binary[y][x - 1] * 1)


                # L     81.15
                lbpImg[y][x] = (binary[y][x - 1] * 128) + (binary[y + 1][x - 1] * 64) + (binary[y + 1][x] * 32) + (
                        binary[y + 1][x + 1] * 16) + (binary[y][x + 1] * 8) + (binary[y - 1][x + 1] * 4) + (
                                       binary[y - 1][x] * 2) + (binary[y - 1][x - 1] * 1)


                # tL    82.31
                lbpImg[y][x] = (binary[y - 1][x - 1] * 128) + (binary[y][x - 1] * 64) + (binary[y + 1][x - 1] * 32) + (
                        binary[y + 1][x] * 16) + (binary[y + 1][x + 1] * 8) + (binary[y][x + 1] * 4) + (
                                       binary[y - 1][x + 1] * 2) + (binary[y - 1][x] * 1)


                # t     84.29
                lbpImg[y][x] = (binary[y - 1][x] * 128) + (binary[y - 1][x - 1] * 64) + (binary[y][x - 1] * 32) + (
                        binary[y + 1][x - 1] * 16) + (binary[y + 1][x] * 8) + (binary[y + 1][x + 1] * 4) + (
                                       binary[y][x + 1] * 2) + (binary[y - 1][x + 1] * 1)


                # tR    83.07
                lbpImg[y][x] = (binary[y - 1][x + 1] * 128) + (binary[y - 1][x] * 64) + (binary[y - 1][x - 1] * 32) + (
                        binary[y][x - 1] * 16) + (binary[y + 1][x - 1] * 8) + (binary[y + 1][x] * 4) + (
                                       binary[y + 1][x + 1] * 2) + (binary[y][x + 1] * 1)



                # ```````````````   Clockwise   ```````````

                # tl    80.46
                lbpImg[y][x] = (binary[y - 1][x - 1] * 128) + (binary[y][x - 1] * 64) + (binary[y + 1][x - 1] * 32) + (
                            binary[y + 1][x] * 16) + (binary[y + 1][x + 1] * 8) + (binary[y][x + 1] * 4) + (
                                           binary[y - 1][x + 1] * 2) + (binary[y - 1][x] * 1)


                # t     83.07
                lbpImg[y][x] = (binary[y][x - 1] * 128) + (binary[y + 1][x - 1] * 64) + (binary[y + 1][x] * 32) + (
                            binary[y + 1][x + 1] * 16) + (binary[y][x + 1] * 8) + (binary[y - 1][x + 1] * 4) + (
                                           binary[y - 1][x] * 2) + (binary[y - 1][x - 1] * 1)

                # tr    81.29
                lbpImg[y][x] = (binary[y + 1][x - 1] * 128) + (binary[y + 1][x] * 64) + (binary[y + 1][x + 1] * 32) + (
                            binary[y][x + 1] * 16) + (binary[y - 1][x + 1] * 8) + (binary[y - 1][x] * 4) + (
                                           binary[y - 1][x - 1] * 2) + (binary[y][x - 1] * 1)
                """
                # r     82.76
                lbpImg[y][x] = (binary[y + 1][x] * 128) + (binary[y + 1][x + 1] * 64) + (binary[y][x + 1] * 32) + (
                            binary[y - 1][x + 1] * 16) + (binary[y - 1][x] * 8) + (binary[y - 1][x - 1] * 4) + (
                                           binary[y][x - 1] * 2) + (binary[y + 1][x - 1] * 1)

                """
                # br    81.23
                lbpImg[y][x] = (binary[y + 1][x + 1] * 128) + (binary[y][x + 1] * 64) + (binary[y - 1][x + 1] * 32) + (
                            binary[y - 1][x] * 16) + (binary[y - 1][x - 1] * 8) + (binary[y][x - 1] * 4) + (
                                           binary[y + 1][x - 1] * 2) + (binary[y + 1][x] * 1)


                # b     81.54
                lbpImg[y][x] = (binary[y][x + 1] * 128) + (binary[y - 1][x + 1] * 64) + (binary[y - 1][x] * 32) + (
                            binary[y - 1][x - 1] * 16) + (binary[y][x - 1] * 8) + (binary[y + 1][x - 1] * 4) + (
                                           binary[y + 1][x] * 2) + (binary[y + 1][x + 1] * 1)


                # bL    79.61
                lbpImg[y][x] = (binary[y - 1][x + 1] * 128) + (binary[y - 1][x] * 64) + (binary[y - 1][x - 1] * 32) + (
                            binary[y][x - 1] * 16) + (binary[y + 1][x - 1] * 8) + (binary[y + 1][x] * 4) + (
                                           binary[y + 1][x + 1] * 2) + (binary[y][x + 1] * 1)


                # L     79.23
                lbpImg[y][x] = (binary[y - 1][x] * 128) + (binary[y - 1][x - 1] * 64) + (binary[y][x - 1] * 32) + (
                            binary[y + 1][x - 1] * 16) + (binary[y + 1][x] * 8) + (binary[y + 1][x + 1] * 4) + (
                                           binary[y][x + 1] * 2) + (binary[y - 1][x + 1] * 1)

                """


                x += 1
            y += 1


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: " + str(error))
        sg.ChangeLookAndFeel('SandyBeach')
        sg.Popup('Exception..', 'thrown in ', str(inspect.stack()[0][3]), str(error))


    finally:
        # f.close()
        return lbpImg


"""
obImg = cv.imread("Obama.png")
#cv.imshow("obImg",obImg)

obHist,bins = np.histogram(obImg.ravel(),256,[0,256])
myHist,bins = np.histogram(obImg.ravel(),256,[0,256])
plt.hist(obHist,  bins=bins)

obLbpImg = lbp(obImg)
#cv.imshow("obLbpImg", obLbpImg)
plt.ion()
obFinal,bins = np.histogram(obImg.ravel(),256,[0,256])
plt.hist(obFinal,  bins=bins)


#print(obFinal)
myImg = cv.imread("mySign2.jpeg")
#cv.imshow("myImg",myImg)
myHist,bins = np.histogram(myImg.ravel(),256,[0,256])
plt.hist(myHist,  bins=bins)

myLbpImg = lbp(myImg)
#cv.imshow("myLbpImg", myLbpImg)
if cv.waitKey():
    cv.destroyAllWindows()

myLbpHist,bins = np.histogram(myImg.ravel(),256,[0,256])
#print(myFinal)
"""


