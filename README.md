# simple-tools
A tool-kit containing simple python scripts for file organization. All scripts can be modified for customized use.

## Contents:

### renameFiles

dateStamp.py - when executed, creates a six digit date stamp at the end of the file name for all files within the same folder _XXXXXX (e.g. _200724 for 2020/07/24).

removeSpaces.py - when executed, remove all spaces in file name and replace with underscore _ for all files within the same folder. 

dateStampNS.py - a combination of dateStamp.py and removeSpaces.py.

### createFolders

createFolders-VideoEditing.py - when executed, creates specified directories useful for video editing projects.

createFolders-Localization.py - when executed, creates specified directories useful for localization projects.

createFolders-Localization_2.0.py - improved by Mateusz Sasinowski.

### OCR

textExtractor-Tesseract.py - need Tesseract to be installed in order for it to work. When executed, extracts text from a designated image (asks for file name and ext) in the same folder and outputs extracted texts into compiler. Updated with character and wordcount.

imageProcessing.py - a script that prepares and cleans up image fors for more accurate OCR scanning.