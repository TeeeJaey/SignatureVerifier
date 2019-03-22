import cv2 as cv
import numpy as np
import imutils
import math
import inspect
from sklearn import svm
import PySimpleGUI as sg


def actualclass(filename, Classes):
    try:
        #f = open("Data/"+datafile, "a")
        result = getClass(filename)

       #f.write("\nActual Class: "+ str(result))
        i = 0
        while (Classes[i] is not None):
            i += 1

        Classes[i] = result

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        #f.write("\nError: "+ str(error))

    finally:
       #f.close()
        return

def getClass(filename):
    try:
        result = filename[:6]

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        #f.write("\nError: "+ str(error))

    finally:
        return result


def knn(trainingFeatures,testingFeatures,trainingClasses,decisionClasses,filename):

    try:
        #f = open("Data/"+datafile, "a")
        i=0
        j=0
        k=22


        while (trainingFeatures[i][j] is not None):
            i += 1
        imageCount = i
        i -= 1
        while (trainingFeatures[i][j] is not None):
            j += 1
        featureCount = j

        x=0
        y=0
        while (testingFeatures[x][y] is not None):
            x += 1
        x -= 1

        distanceVector = [99999 for x in range(imageCount)]

        trainingClass2 = trainingClasses.copy()

        i=0
        while(i < imageCount):      # Calculate Distance list
            j=0
            total=0
            while(j < featureCount):
                temp = trainingFeatures[i][j] - testingFeatures[x][j]
                temp = temp*temp
                total = total + temp
                j+=1
            distanceVector[i] = math.sqrt(total)
            i+=1

        #get = False
        #if (x % 3 != 0 and x % 4 != 0): get = True

        j=0
        while(j < imageCount):      # Sorting Distance list
            min = distanceVector[j]
            minIndex = j
            i=j+1
            while(i < imageCount):
                if(distanceVector[i] < min):
                    min = distanceVector[i]
                    minIndex = i
                i+=1
            distanceVector[j],distanceVector[minIndex] = distanceVector[minIndex],distanceVector[j]
            trainingClass2[j],trainingClass2[minIndex] = trainingClass2[minIndex],trainingClass2[j]
            j+=1


        i=0
        trainingClass2 = trainingClass2[0:k]
        trainingClass3 = [None for x in range(k)]
        trainingClassCount = []

        while(i<k):                 # Calculating Class Count
            decisionClass = trainingClass2[i]
            j=0
            while(j<k):
                if(trainingClass3[j] != None):
                    if(trainingClass3[j]==decisionClass):
                        trainingClassCount[j] += 1
                        j+=1
                        break
                else:
                    trainingClass3[j] = decisionClass
                    trainingClassCount.append(1)
                    j+=1
                    break
                j+=1
            i+=1


        max = trainingClassCount[0]
        maxIndex = 0
        i = 1
        while (i < len(trainingClassCount)):            # Find maximum ClassCount and corresponding Class
            if (trainingClassCount[i] > max):
                max = trainingClassCount[i]
                maxIndex = i
            i+=1

        nearest = distanceVector[0]
        ActualClass  = getClass(filename)
        if(nearest <= 10):
            decisionClass = trainingClass2[0]
        else:
            decisionClass = trainingClass3[maxIndex]

        if(ActualClass[:1] == decisionClass[:1] and decisionClass[2:]=="orig"):
            decision = "Accepted"
        else:
            decision = "Rejected"

        x=0
        while(decisionClasses[x] is not None):
            x+=1

        decisionClasses[x] = decision
        print("Decision: ",decisionClasses[x])
        #f.write("\nDecision: " + str(decisionClass))


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.ChangeLookAndFeel('SandyBeach')
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))


    finally:
       #f.close()
        return

