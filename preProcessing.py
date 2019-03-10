import cv2 as cv
import numpy as np
import imutils
import math
import inspect
import PySimpleGUI as sg

def boundaryBox(img):

    try:
        #f = open("Data/"+datafile, "a")
        height = img.shape[0]
        width = img.shape[1]
        found=False
        y=0
        while(y<height):
            x=0
            while(x < width):
                if(img[y][x]==0):
                    found=True
                    break
                x+=1
            if(found):
                break
            y+=1
        top = y

        found=False
        y=height-1
        while(y > 0):
            x=width-1
            while(x > 0):
                if(img[y][x]==0):
                    found=True
                    break
                x-=1
            if(found):
                break
            y-=1
        bottom = y

        found=False
        x=0
        while(x < width):
            y=0
            while(y < height):
                if(img[y][x]==0):
                    found=True
                    break
                y+=1
            if(found):
                break
            x+=1
        left = x

        found=False
        x=width-1
        while(x > 0):
            y=height-1
            while(y > 0):
                if(img[y][x]==0):
                    found=True
                    break
                y-=1
            if(found):
                break
            x-=1
        right = x

        img = img[top:bottom,left:right]

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
       #f.write("\nError: "+ str(error))

    finally:
       #f.close()
        return top , bottom , left , right


def preprocess(orgImg):

    try:

        print()
        if(len(orgImg.shape)>2):
            orgImg = cv.cvtColor(orgImg, cv.COLOR_RGB2GRAY)

        orgImg = imutils.resize(orgImg, 720)

        # ~~ Otsu's thresholding after Gaussian filtering ~~
        blur = cv.GaussianBlur(orgImg,(3,3),0)
        ret, img = cv.threshold(blur,0,255,cv.THRESH_OTSU)

        top, bottom, left, right = boundaryBox(img)

        orgImg = orgImg[top:bottom,left:right]
        img = img[top:bottom,left:right]


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))

    finally:
        return orgImg , img
