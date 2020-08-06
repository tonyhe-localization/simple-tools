# script that cleans up images (pre-process) before OCR.

import cv2
import numpy as np

img = cv2.imread(input("Please enter name of the image file you'd like to have pre-processed: "))

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)