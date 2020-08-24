# when executed, zips each file within a folder individually. Very useful for working on multilingual files and folders.

import zipfile
import os

path = os.getcwd() 
os.chdir(path) 

print("The following files will be zipped:")
print(os.listdir())

for folder in os.listdir():
    f_name, f_ext = os.path.splitext(folder)
    '''
    file_root = os.path.splitext(file)[0]
    zip_file_name = file_root + '.zip'
    with zipfile.ZipFile(zip_file_name, mode='w') as zf:
        zf.write(file)
    '''
    if f_name == 'quickZip' and f_ext == '.py':
        print('Skipping quickZip...')
    else:
        zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(os.path.join(path, folder)):
            for filename in files:
                zipf.write(os.path.abspath(os.path.join(root, filename)),arcname=filename)
        zipf.close()

