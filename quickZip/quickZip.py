# when executed, zips each file within a folder individually. Very useful for working on multilingual files and folders.

import zipfile
import os

path = os.getcwd() 
os.chdir(path) 

print("The following files will be zipped:")
print(os.listdir())

for file in os.listdir():
    file_root = os.path.splitext(file)[0]
    zip_file_name = file_root + '.zip'
    with zipfile.ZipFile(zip_file_name, mode='w') as zf:
        zf.write(file)