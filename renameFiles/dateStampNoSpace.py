# Once executed, removes and replaces all spaces in file name, replaces with "_" underscores, and creates a date stamp for all files within the same folder.

import os
from datetime import datetime
import re

def removeSpaces(i):
    def urlify(fileName): # borrowed from stack overflow

        # Remove all non-word characters (everything except numbers and letters)
        fileName = re.sub(r"[^\w\s]", '', fileName)

        # Replace all runs of whitespace with underscores
        fileName = re.sub(r"\s+", '_', fileName) # this can also be modified to replace whitespace with dashes "-".

        return fileName


    path = os.getcwd()
    os.chdir(path)

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)

        if f_name == 'dateStamp' and f_ext == '.py': # skip the "dateStamp.py" script itself.
            print('Skipping dateStamp...')
        elif f_ext == '.ini': # skip any .ini files that you don't want to change the name to.
            print('Skipping ini file...')

        else:
            new_name = '{}{}'.format(urlify(f_name), f_ext)
            os.rename(f, new_name)
    return(i)

