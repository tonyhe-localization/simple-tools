# when executed, zips each file within a folder individually. Very useful for working on multilingual files and folders.

from zipfile 
import os

path = os.getcwd()
os.chdir(path)

for f in os.listdir():
    newZip = zipfile.ZipFile("", "a") # "a" to append, "w" to write.
    
