# script that cleans up images (pre-process) before OCR.

import cv2
import pytesseract

img = cv2.imread(input("Please enter name of the image file you'd like to have pre-processed: "))