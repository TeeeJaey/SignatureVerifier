# SignatureVerifier - Python project

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2000px-Python-logo-notext.svg.png" height="200"  align="right" style="float:right" />

- SignatureVerifier is a project that runs on [Python 3.X](https://www.python.org/downloads/release/python-366/) and [MySQL](https://www.mysql.com/)
- Performs Handwritten signature Verification
- Uses [Image Processing](https://www.tutorialspoint.com/dip/image_processing_introduction.htm) and [Machine Learning](https://www.tutorialspoint.com/machine_learning_with_python/index.html)

  
## Requirements 
| Python | Package |
| --- | --- |
| cv2        | [![OpenCV](https://badge.fury.io/py/opencv-python.svg)](https://pypi.org/project/opencv-python/) |
| numpy      | [![numpy](https://badge.fury.io/py/numpy.svg)](https://pypi.org/project/numpy/)                  |
| imutils    | [![imutils](https://badge.fury.io/py/imutils.svg)](https://pypi.org/project/imutils/)            |
| pymysql    | [![PyMySQL](https://badge.fury.io/py/PyMySQL.svg)](https://pypi.org/project/PyMySQL/)            |
| os         | [![os](https://badge.fury.io/py/os-win.svg)](https://pypi.org/project/os-win/)                   |
| scipy      | [![scipy](https://badge.fury.io/py/scipy.svg)](https://pypi.org/project/scipy/)                  |
| mahotas    | [![mahotas](https://badge.fury.io/py/mahotas.svg)](https://pypi.org/project/mahotas/)            |
| matplotlib | [![matplotlib](https://badge.fury.io/py/matplotlib.svg)](https://pypi.org/project/matplotlib/)   |
| easygui    | [![easygui](https://badge.fury.io/py/easygui.svg)](https://pypi.org/project/easygui/)            |


## Theory

<img src="https://raw.githubusercontent.com/TeeeJaey/SignatureVerifier/master/preProcessing.JPG" height="140"  align="right" style="float:right" />

System works in 3 stages : 
- Data conversion
- Preprocessing
- LBP image generation
- Feature Extraction
- Classification


## Material

<img src="https://raw.githubusercontent.com/TeeeJaey/SignatureVerifier/master/lbp.JPG" height="200"  align="right" style="float:right" />

Contains python code for :
- Main function
- Preprocessing
- Shape features
- GLCM features
- Texture Features
- LBP image generation
- Classification
- Dataset analysis

Contains data set of :
<img src="https://raw.githubusercontent.com/TeeeJaey/SignatureVerifier/master/DataSource.JPG" height="300"  align="right" style="float:right" />
- 25 signers
- 50 Classes
- 826 Images
- 637 Training images (77.12%)
- 189 Testing images (22.88%)


## References 

- Dataset was obtained from [http://www.iapr-tc11.org](http://www.iapr-tc11.org/mediawiki/index.php?title=Datasets_List#Handwritten%20Documents#Graphical%20%20Documents)
