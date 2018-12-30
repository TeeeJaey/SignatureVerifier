# SignatureVerifier - Python project

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2000px-Python-logo-notext.svg.png" height="200"  align="right" style="float:right" />

- SignatureVerifier is a project that runs on python 3.X
- Performs Handwritten signature Verification and author identification.
- Uses Image Processing [Image Processing](https://www.tutorialspoint.com/dip/image_processing_introduction.htm) and [Machine Learning](https://www.tutorialspoint.com/machine_learning_with_python/index.html)


  
## Requiremnts

- cv2 [![OpenCV](https://badge.fury.io/py/opencv-python.svg)](https://pypi.org/project/opencv-python/)
- numpy [![numpy](https://badge.fury.io/py/numpy.svg)](https://pypi.org/project/numpy/)
- imutils  [![imutils](https://badge.fury.io/py/imutils.svg)](https://pypi.org/project/imutils/)
- os  [![os](https://badge.fury.io/py/os-win.svg)](https://pypi.org/project/os-win/)
- scipy  [![scipy](https://badge.fury.io/py/scipy.svg)](https://pypi.org/project/scipy/)
- mahotas  [![mahotas](https://badge.fury.io/py/mahotas.svg)](https://pypi.org/project/mahotas/)
- matplotlib [![matplotlib](https://badge.fury.io/py/matplotlib.svg)](https://pypi.org/project/matplotlib/)


## Theory

<img src="preProcessing.jpg" height="150"  align="right" style="float:right" />

System works in 3 stages : 
- Preprocessing
- Feature Extraction
- Classification

## Material
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
- 25 signers
- 50 Classes
- 826 Images
- 637 Training images (77.12%)
- 189 Testing images (22.88%)
