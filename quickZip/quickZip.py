# when executed, zips each file within a folder individually. Very useful for working on multilingual files and folders.

import zipfile
import os

# everything happens in the current directory
path = os.getcwd() 
os.chdir(path) 

print("The following files will be zipped:")
print(os.listdir()) # check

# zip every file in the folder individually
for folder in os.listdir():
    f_name, f_ext = os.path.splitext(folder)

    if f_name == 'quickZip' and f_ext == '.py':
        print('Skipping quickZip...')
    elif f_ext == '.ini':
        print('Skipping .ini files...')
    elif f_ext == '.py':
        print('Skipping .py files...')
    elif f_ext == '.zip':
        print('Skipping .zip files...')
    else:
        zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(os.path.join(path, folder)):
            for filename in files:
                zipf.write(os.path.abspath(os.path.join(root, filename)),arcname=filename)
        zipf.close()

