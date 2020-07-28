# This is a quick script used to create folders for L10N projects. May need some customization based on langs.


import os

path = os.getcwd()

path_1 = path + "/folder_temp/helper/source"
path_2 = path + "/folder_temp/helper/target"
path_3 = path + "/folder_temp/source/en_US"
path_4 = path + "/folder_temp/source/zh_CN"
path_5 = path + "/folder_temp/target/en_US"
path_6 = path + "/folder_temp/target/en_US"

print("The current working directory is %s" % path)


try:
    os.makedirs(path_1)

except OSError:
    print ("Creation of the directory %s failed" % path_1)

else:
    print("Successfully created the directory %s" % path_1)
    

try:
    os.makedirs(path_2)

except OSError:
    print ("Creation of the directory %s failed" % path_2)

else:
    print("Successfully created the directory %s" % path_2)
    

try:
    os.makedirs(path_3)

except OSError:
    print ("Creation of the directory %s failed" % path_3)

else:
    print("Successfully created the directory %s" % path_3)


try:
    os.makedirs(path_4)

except OSError:
    print ("Creation of the directory %s failed" % path_4)

else:
    print("Successfully created the directory %s" % path_4)


try:
    os.makedirs(path_5)

except OSError:
    print ("Creation of the directory %s failed" % path_5)

else:
    print("Successfully created the directory %s" % path_5)

try:
    os.makedirs(path_6)

except OSError:
    print ("Creation of the directory %s failed" % path_6)

else:
    print("Successfully created the directory %s" % path_6)


    
