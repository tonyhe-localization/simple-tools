# Once executed, removes and replaces all spaces in file name, replaces with "_" underscores, and creates a date stamp for all files within the same folder.

import os
from datetime import datetime
import re

def removeSpaces():
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

        if f_name == 'dateStampNS' and f_ext == '.py': # skip the "dateStamp.py" script itself.
            print('Skipping dateStamp...')
        elif f_ext == '.ini': # skip any .ini files that you don't want to change the name to.
            print('Skipping ini files...')
        elif f_ext == '.py':
            print('Skipping .py files...')

        else:
            new_name = '{}{}'.format(urlify(f_name), f_ext)
            os.rename(f, new_name)

def dateStamp():
    # Get today's date and remove the dashes and the first two digits "20".
    date = datetime.date(datetime.now()).strftime('%Y%m%d') [2:] # This format can be modified.
    #print(date) check

    # Rename a file in the Downloads folder to something specific.
    path = os.getcwd()
    os.chdir(path)

    # For any file f in the following list of directories, add date stamp after file name.
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)

        if f_name == 'dateStampNS' and f_ext == '.py': 
            print('Skipping dateStamp...')
        elif f_name == 'removeSpaces' and f_ext == '.py': 
            print('Skipping removeSpaces.py...')
        elif f_name == 'dateStampNoSpace' and f_ext == '.py':
            print('Skipping dateStampNoSpace.py')

        elif f_ext == '.ini': # skip any .ini files that you don't want to change the name to.
            print('Skipping ini file...')
        elif f_ext == '.py':
            print('Skipping .py files...')
        else:
            new_name = '{}_{}{}'.format(f_name, date, f_ext)
            os.rename(f, new_name)

removeSpaces()
dateStamp()
