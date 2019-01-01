import cv2 as cv
import numpy as np
import imutils
import os
import math
from matplotlib import pyplot as plt

def lbp(img):
        if(len(img.shape)>2):
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        img = imutils.resize(img, 720)
        binary = img.copy()
        lbpImg = img.copy()
        height = img.shape[0]
        width = img.shape[1]
        
        y=1
        while(y<height-1):
            x=1
            while(x < width-1):
                binary[y-1][x-1] = 1 if(img[y-1][x-1] < img[y][x]) else 0
                binary[y-1][x] = 1 if(img[y-1][x] < img[y][x]) else 0
                binary[y-1][x+1] = 1 if(img[y-1][x+1] < img[y][x]) else 0
                
                binary[y][x-1] = 1 if(img[y][x-1] < img[y][x]) else 0
                binary[y][x+1] = 1 if(img[y][x+1] < img[y][x]) else 0

                binary[y+1][x-1] = 1 if(img[y+1][x-1] < img[y][x]) else 0
                binary[y+1][x] = 1 if(img[y+1][x] < img[y][x]) else 0
                binary[y+1][x+1] = 1 if(img[y+1][x+1] < img[y][x]) else 0
                
                lbpImg[y][x] = (binary[y][x-1]*128) + (binary[y-1][x-1]*64) + (binary[y-1][x]*32) + (binary[y-1][x+1]*16) + (binary[y][x+1]*8) + (binary[y+1][x+1]*4) + (binary[y+1][x]*2) + (binary[y+1][x-1]*1)
                #lbpImg[y][x] = (binary[y-1][x+1]*128) + (binary[y][x+1]*64) + (binary[y+1][x+1]*32) + (binary[y+1][x]*16) + (binary[y+1][x-1]*8) + (binary[y][x-1]*4) + (binary[y-1][x-1]*2) + (binary[y-1][x]*1)
                x+=1
            y+=1
            
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