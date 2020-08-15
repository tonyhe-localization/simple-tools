import os

folder_name = input("Please enter folder name: ")        
path_1 = os.path.join(os.getcwd(), folder_name, 'helper/source')   
path_2 = os.path.join(os.getcwd(), folder_name, 'helper/target') 
path_3 = os.path.join(os.getcwd(), folder_name, 'source/en_US') 
path_4 = os.path.join(os.getcwd(), folder_name, 'source/zh_CN') 
path_5 = os.path.join(os.getcwd(), folder_name, 'target/en_US')
path_6 = os.path.join(os.getcwd(), folder_name, 'target/zh_CN') 

print("The current working directory is %s" % os.getcwd())

for path in [path_1, path_2, path_3, path_4, path_5, path_6]:    
    try: 
        os.makedirs(path)
    except OSError:
        print(f"Creation of the directory {path} failed")    
    else:
        print(f"Successfully created the directory {path}")
