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
val = [2,"Tejas", 3.45]
trainingFeatures = [[1.02, 23.12,102.3, None],
                    [2.22, 32.7, 121.0, None],
                    [3.10, 39.5, 131.3, None],
                    [4.10, 49.5, 141.3, None],
                    [5.10, 39.5, 131.3, None],
                    [6.10, 59.5, 151.3, None],
                    [None, None, None, None]]

val.clear()
ImageID = "A_forged_1"
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
