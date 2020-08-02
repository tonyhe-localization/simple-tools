# Uses tesseract to extract texts from images.

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os
from PIL import Image

# input image name (copy and paste) and print text.
new_image = input("Please enter the image file name with file extension: ")
inputLang = input("Please enter the language of the file ('eng' for English, 'chi_sim' for Simplified Chinese, etc.): ")

custom_oem_psm_config = r'--oem 3 --psm 11'# custom configurations.

image = Image.open(new_image)
text = tess.image_to_string(image, lang = inputLang, config = custom_oem_psm_config)

print("Extracted words below:")
print(text)

wordCount = print(len(text))
