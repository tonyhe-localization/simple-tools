# when executed, zips each file within a folder individually. Very useful for working on multilingual files and folders.

from zipfile import ZipFile
import os

def filePaths(directory):
    path = os.getcwd()
    os.chdir(path)

    for f in os.listdir():
        