# %% [markdown]
# # Reading a Screenshot using OCR
# Computer Vision

# %% [markdown]
# ## Requirements for this notebook
# - [pytesseract](https://pypi.org/project/pytesseract/)
# - [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) (for Windows)
# - [cv2](https://pypi.org/project/opencv-python/)
# - [numpy](https://pypi.org/project/numpy/)

# %%
from matplotlib import pyplot as plt # For developing only
import cv2
import pytesseract
import re
import numpy as np

# %% [markdown]
# For showing the image in the notebook

# %% [markdown]
# ### Steps to execute the reading of a screenshot
# 1. Import the required libraries
# 2. Read the image using cv2
# 3. Use function preprocessing() to convert the image to grayscale and add a threshold
# 4. Before using the read_photo() function and pass the image as a parameter. (make sure to change the path to the tesseract.exe file). This will get all the text from the image.
# 5. Lastly, to get the desired test use the get_lines_needed() function and pass the text as a parameter. This will return a list of strings, contains the important information from the image.

# %%
def preprocessing(img):
    """Converts the image to grayscale and add Threshold"""
    
    # This enhances the image
    dst = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15) # This enhances the detail of the photo
    
    # This converts the image to grayscale
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # Converts to grayscale
    
    t,thresh = cv2.threshold(gray, 0, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C | cv2.THRESH_OTSU)# Add threshold
    # invert the threshold
    thresh = cv2.bitwise_not(thresh)
    
    # This is the kernel used for dilation and erosion of the image to remove noise and enhances the 
    kernel = np.ones((1, 1), np.int8)
    # dilate the image
    dilete = cv2.dilate(thresh,kernel,iterations = 3)
    # expand the layer or the dark spot
    # This is for debugging purposes


    return dilete

# %%
def read_photo(image):
    """Reads the image and returns the text in the image"""
    # this is the path to the tesseract executable file
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image)
    return text

# %%

def get_lines_needed(raw_image):
    """Returns the lines needed for the report"""
    # Regex pattern to get the lines needed
    # Read the image using imread
    raw_image = cv2.imread("1.png")

    # Regex pattern to get the lines needed
    pattern1= re.compile(r"(\(Team\) ([A-Za-z0-9\! ]+\w): ([A-Za-z0-9\! ]+\w))") # Format: (Team) username: message
    pattern2= re.compile(r"(\(Party\) ([A-Za-z0-9\! ]+\w): ([A-Za-z0-9\! ]+\w))")
    pattern3= re.compile(r"([A-Za-z0-9\! \(\)]+\w)")

    # Preprocessing the image to make it clear for the detection and read it properly
    prepro = preprocessing(raw_image)
    
    # Read the image and split it by lines to make it a array
    lines = read_photo(prepro).split("\n")
    # Get the lines needed for the report
    team= [line for line in lines if pattern1.match(line)]
    party= [line for line in lines if pattern2.match(line)]
    alls= [line for line in lines if pattern3.match(line)]

    # Return the lines needed
    return team

# %%
# get_lines_needed("1.png")

# # %%
# get_lines_needed("4.png")

# %%



