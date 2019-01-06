import cv2 as cv
import imutils
import numpy as np
import math
from tkinter import *
from scipy import ndimage
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy.stats import entropy
import mahotas as mt
import inspect

from skimage import feature

def divByZ():
    try:
        divideByZero = 10/0
        print(divideByZero)

    except Exception as error:
        print("An exception was thrown in "+ inspect.stack()[0][3])
        print("Error: ", str(error))

    finally:
        print("Finally")
        return


divByZ()