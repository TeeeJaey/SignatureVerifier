import cv2 as cv
import numpy as np
import imutils
import math

def boundaryBox(img):
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

    return img


def preprocess(img):

    """
    cv.imshow("read", Img)

    width = 400
    height = img.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA) # resize image
    cv.imshow("Resized image", resized)

    img = cv.fastNlMeansDenoising(img, None, 18, 7, 21)
    Th =  220

    ret,img = cv.threshold(img, Th, 255, cv.THRESH_BINARY)
    img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    """

    img = imutils.resize(img, 720)
    print()
    if(len(img.shape)>2):
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # ~~ Otsu's thresholding after Gaussian filtering ~~
    blur = cv.GaussianBlur(img,(3,3),0)
    ret, img = cv.threshold(blur,0,255,cv.THRESH_OTSU)

    img = boundaryBox(img)
    return img

