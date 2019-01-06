import cv2 as cv
import numpy as np
import imutils
import math
import inspect

def actualclass(filename, Classes, datafile):
    try:
        f = open("Data/"+datafile, "a")
        if "genuine" in filename: result = filename[:9]
        if "forged" in filename: result = filename[:8]
        """
        result = 0
        if "genuine" in filename: result +=100
        if "A_" in filename: result +=1
        elif "B_" in filename: result +=2
        elif "C_" in filename: result +=3
        elif "D_" in filename: result +=4
        elif "E_" in filename: result +=5
        elif "F_" in filename: result +=6
        elif "G_" in filename: result +=7
        elif "H_" in filename: result +=8
        elif "I_" in filename: result +=9
        elif "J_" in filename: result +=10
        elif "K_" in filename: result +=11
        elif "L_" in filename: result +=12
        elif "M_" in filename: result +=13
        elif "N_" in filename: result +=14
        elif "O_" in filename: result +=15
    
        """

        print("Actual Class: ", result)
        f.write("\nActual Class: "+ str(result))
        i = 0
        while (Classes[i] is not None):
            i += 1

        Classes[i] = result

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("\nError: "+ str(error))

    finally:
        f.close()
        return


def knn(trainingFeatures,testingFeatures,trainingClass, datafile):

    try:
        f = open("Data/"+datafile, "a")
        i=0
        j=0
        k=5

        while (trainingFeatures[i][j] is not None):
            i += 1
        imageCount = i
        i -= 1
        while (trainingFeatures[i][j] is not None):
            j += 1
        featureCount = j

        #featureCount = len(trainingFeatures[0])

        distanceVector = [None for x in range(imageCount)]

        trainingClass2 = trainingClass.copy()

        i=0
        while(i < imageCount):      # Calculate Distance list
            j=0
            total=0
            while(j < featureCount):
                temp = trainingFeatures[i][j] - testingFeatures[j]
                temp = temp*temp
                total = total + temp
                j+=1
            distanceVector[i] = math.sqrt(total)
            i+=1


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

        decisionClass = trainingClass3[maxIndex]

        print("Decision: ",decisionClass)
        f.write("\nDecision: " + str(decisionClass))

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        f.write("\nError: "+ str(error))

    finally:
        f.close()
        return

"""

trainingFeatures = [[1.02, 23.12,102.3, None],
                    [2.22, 32.7, 121.0, None],
                    [3.10, 39.5, 131.3, None],
                    [4.10, 49.5, 141.3, None],
                    [5.10, 39.5, 131.3, None],
                    [6.10, 59.5, 151.3, None],
                    [None, None, None, None]]
testingFeatures = [3,40,130, None]
trainingClass = ["A","A","C","A","B","D"]

knn(trainingFeatures,testingFeatures,trainingClass)

"""