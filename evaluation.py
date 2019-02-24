import cx_Oracle as oracle
import cv2 as cv
import pymysql

def evaluate():
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="signature_verifier" )
    cur = connection.cursor()
    cur.execute('''SELECT * FROM testing_classes''')
    total = 0
    correct = 0
    for result in cur:
        print( result )
        if(result[1] == result[2]):
            correct+=1
        total+=1
    connection.autocommit(True)
    connection.close()
    accuracy = correct * 100 / total
    print ("Accuracy : " , accuracy )

    print()
    return
