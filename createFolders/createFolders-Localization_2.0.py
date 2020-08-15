# with further contributions from Mateusz Sasinowski, logged on 6/10/2020

import os

folder_name = input("Please decide on a folder's name: ")        
path_1 = os.path.join(os.getcwd(), folder_name, 'helper/source')    # .join method to add user's folder name to the file structure
path_2 = os.path.join(os.getcwd(), folder_name, 'helper/target') 
path_3 = os.path.join(os.getcwd(), folder_name, 'source/en_US') 
path_4 = os.path.join(os.getcwd(), folder_name, 'source/zh_CN') 
path_5 = os.path.join(os.getcwd(), folder_name, 'target/en_US')
path_6 = os.path.join(os.getcwd(), folder_name, 'target/zh_CN') 

print("The current working directory is %s" % os.getcwd())

for path in [path_1, path_2, path_3, path_4, path_5, path_6]:    # simplified into a single loop for any number of folders
    try: 
        os.makedirs(path)
    except OSError:
        print(f"Creation of the directory {path} failed")     # changed for f"" string literal method as good practice
    else:
        print(f"Successfully created the directory {path}")
