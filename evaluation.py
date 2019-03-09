import cx_Oracle as oracle
import cv2 as cv
import pymysql
import inspect
import PySimpleGUI as sg


def evaluate():

    try:
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="signature_verifier")
        cur = connection.cursor()
        cur.execute('''SELECT * FROM testing_classes''')
        total = 0
        correct = 0
        FAR = 0
        FRR = 0

        for result in cur:
            print(result)
            actualClass = result[1]

            if (actualClass[2:] == "orig" and result[2] == "Accepted"):
                correct += 1
            elif (actualClass[2:] == "forg" and result[2] == "Rejected"):
                correct += 1
            elif(actualClass[2:] == "orig" and result[2] == "Rejected"):
                FRR += 1
            elif(actualClass[2:] == "forg" and result[2] == "Accepted"):
                FAR += 1
            total += 1

        connection.autocommit(True)
        connection.close()
        accuracy = correct * 100 / total
        dFAR = FAR * 100 / total
        dFRR = FRR * 100 / total
        print(accuracy)

        sg.ChangeLookAndFeel('SandyBeach')

        szFAR = 'FAR : ' + str(dFAR) + '%'
        szFRR = 'FRR : ' + str(dFRR) + '%'
        szAccuracy = 'Accuracy : ' + str(accuracy) + '%'

        sg.Popup('Perfomace Measure',szFAR, szFRR, szAccuracy)

    except Exception as error:
        print("An exception was thrown in " + inspect.stack()[0][3])
        #f = open("Data/"+datafile, "a")
        print("Error: "+ str(error))
       #f.write("\nError: "+ str(error))
       #f.close()

    finally:
        return






