# %% [markdown]
# # Reading a Screenshot using OCR
# Computer Vision

# %% [markdown]
# ## Requirements for this notebook
# - [pytesseract](https://pypi.org/project/pytesseract/)
# - [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) (for Windows)
# - [cv2](https://pypi.org/project/opencv-python/)
# - [imutils](https://pypi.org/project/imutils/)
# - [numpy](https://pypi.org/project/numpy/) (Optional)

# %%
import imutils
import cv2
import pytesseract
import re

# %% [markdown]
# ### Steps to execute the reading of a screenshot
# 1. Import the required libraries
# 2. Read the image using cv2
# 3. Use function pre_gray() to convert the image to grayscale and add a threshold
# 4. Before using the read_photo() function and pass the image as a parameter. (make sure to change the path to the tesseract.exe file). This will get all the text from the image.
# 5. Lastly, to get the desired test use the get_lines_needed() function and pass the text as a parameter. This will return a list of strings, contains the important information from the image.

# %%
def read_photo(image):
    """Reads the image and returns the text in the image"""
    # this is the path to the tesseract executable file
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image)
    return text

# %%

def pre_gray(img):
    """Converts the image to grayscale and add Threshold"""
    
    # This enhances the image
    dst = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    
    # This converts the image to grayscale
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # Converts to grayscale
    
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] # Add threshold
    
    # This is for debugging purposes
    # cv2.imshow("thresh.png", gray)
    # cv2.waitKey(0)
    return thresh

# %%

def get_lines_needed(raw_text):
    """Returns the lines needed for the report"""
    # Regex pattern to get the lines needed
    pattern= re.compile(r"(\(Team\) ([A-Za-z0-9\! ]+\w): ([A-Za-z0-9\! ]+\w))") # Format: (Team) username: message
    # Preprocessing the image to make it clear for the detection and read it properly
    prepro = pre_gray(raw_text)
    # Read the image and split it by lines to make it a array
    lines = read_photo(prepro).split("\n")
    # Get the lines needed for the report
    cleaned_text= [line for line in lines if pattern.match(line)]
    # Return the lines needed
    return cleaned_text

# %%


