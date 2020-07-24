# Once executed, creates a date stamp for all files within the same folder.

import os
from datetime import datetime

# Get today's date and remove the dashes and the first two digits "20".
date = datetime.date(datetime.now()).strftime('%Y%m%d') [2:]
#print(date) check

# Rename a file in the Downloads folder to something specific.
path = os.getcwd()
os.chdir(path)

# For any file f in the following list of directories, add date stamp after file name.
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    if f_name == 'dateStamp' and f_ext == '.py': # skip "dateStamp.py" file itself.
        print('Skipping dateStamp...')
    elif f_ext == '.ini': # skip any .ini files that you don't want to change the name to.
        print('Skipping ini file...')
    
    else:
        new_name = '{}_{}{}'.format(f_name, date, f_ext)
        os.rename(f, new_name)
    
         
