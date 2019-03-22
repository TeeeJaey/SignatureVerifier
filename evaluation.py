import cx_Oracle as oracle
import cv2 as cv
import pymysql
import inspect
import PySimpleGUI as sg
import os


def evaluate():

    try:

        sg.ChangeLookAndFeel('SandyBeach')
        # database connection
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="signature_verifier")
        cur = connection.cursor()
        cur.execute('''SELECT * FROM testing_classes''')
        if (cur.rowcount == 0):
            sg.Popup('Error!','We need to test our data first!')
            print ("\nError! We need to test data first!")
            return

        total = 0
        FAR = 0
        FRR = 0

        for result in cur:
            print(result)
            actualClass = result[1]

            if(actualClass[2:] == "orig" and result[3] == "Rejected"):
                FRR += 1
            elif(actualClass[2:] == "forg" and result[3] == "Accepted"):
                FAR += 1
            total += 1

        connection.autocommit(True)
        connection.close()

        dFAR = FAR * 100 / total
        dFRR = FRR * 100 / total
        dAccuracy = 100.0 - (dFAR + dFRR)

        szFAR = 'False Acceptance Rate : ' + str(round(dFAR, 2)) + ' %'
        szFRR = 'False Rejection Rate :  ' + str(round(dFRR, 2)) + ' %'
        szAccuracy = 'Accuracy of the system : ' + str(round(dAccuracy, 2)) + ' %'

        print()
        print(szFAR)
        print(szFRR)
        print(szAccuracy)
        sg.Popup('Evaluation',szFAR, szFRR, szAccuracy)


    except Exception as error:
        print("An exception in " + inspect.stack()[0][3])
        print("Error: "+ str(error))
        sg.ChangeLookAndFeel('SandyBeach')
        sg.Popup('Exception..','thrown in ',str(inspect.stack()[0][3]),str(error))


    finally:
        return




