import cx_Oracle as oracle
import cv2 as cv
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="signature_verifier" )
cur = connection.cursor()
# some other statements  with the help of cursor
"""
cur.execute('''CREATE TABLE IF NOT EXISTS `training_features` (
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `AspectRatio` float(10,5) NOT NULL,
  `X_CoG` float(10,5) NOT NULL,
  `Y_CoG` float(10,5) NOT NULL,
  `NormalisedArea` float(10,5) NOT NULL,
  `BaselineShift` float(10,5) NOT NULL,
  `Eccentricity` float(10,5) NOT NULL,
  `HuMoments` float(10,5) NOT NULL,
  `Contrast` float(10,5) NOT NULL,
  `Dissimilarity` float(10,5) NOT NULL,
  `Homogeneity` float(10,5) NOT NULL,
  `Energy` float(10,5) NOT NULL,
  `Correlation` float(10,5) NOT NULL,
  `ASM` float(10,5) NOT NULL,
  `Mean` float(10,5) NOT NULL,
  `Variance` float(10,5) NOT NULL,
  `Skewness` float(10,5) NOT NULL,
  `Kurtosis` float(10,5) NOT NULL,
  `Entropy` float(10,5) NOT NULL,
  `Haralick` float(10,5) NOT NULL
  )''')

ImageID = 'A_forged_1'
select = "SELECT * FROM training_features WHERE ImageID = %s"
cur.execute(select,"A_forged_1")


cur.execute('''CREATE TABLE IF NOT EXISTS `MyFriends` (ID INT(10) PRIMARY KEY AUTO_INCREMENT, FNAME CHAR(20) NOT NULL, CGPA FLOAT(3.2) )''')

cur.execute('''Insert into MyFriends values (1,'Malak',3.21)''')

sql = "insert into MyFriends values (%s, %s, %s)"
"""
trainingFeatures = [[1.02, 23.12,102.3, None],
                    [2.22, 32.7, 121.0, None],
                    [3.10, 39.5, 131.3, None],
                    [4.10, 49.5, 141.3, None],
                    [5.10, 39.5, 131.3, None],
                    [6.10, 59.5, 151.3, None],
                    [None, None, None, None]]

val = []
val.clear()
filename = "A_forged_1.png"
ImageID = filename[:-4]
val.append(ImageID)
j = 0
i = 0
while (trainingFeatures[i][j] is not None):
  i += 1

i -= 1
while (trainingFeatures[i][j] is not None):
  val.append(trainingFeatures[i][j])
  j += 1

print(val)

"""
cur.execute(sql, val)

cur.execute('''SELECT * FROM MyFriends''')

for result in cur:
    print("Friends: ", result )

connection.autocommit(True)
connection.close()

"""
# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read the image
img = cv2.imread('mySign.jpeg')

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
cornersPts = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
cornersPts = np.int0(cornersPts)
corners=0
# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in cornersPts:
    corners+=1
print(corners)