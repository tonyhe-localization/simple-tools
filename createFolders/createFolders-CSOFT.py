import os

folder_name = input("Please enter folder name: ")        
path_1 = os.path.join(os.getcwd(), folder_name, 'Engineering/To_DTP')
path_2 = os.path.join(os.getcwd(), folder_name, 'Engineering/To_PM')   
path_3 = os.path.join(os.getcwd(), folder_name, 'Engineering/Trans_Kit')
path_4 = os.path.join(os.getcwd(), folder_name, 'From_Client/Comments')
path_5 = os.path.join(os.getcwd(), folder_name, 'Hand_Off/To_Trans')
path_6 = os.path.join(os.getcwd(), folder_name, 'Hand_Off/From_Trans')
path_7 = os.path.join(os.getcwd(), folder_name, 'PO/')
path_8 = os.path.join(os.getcwd(), folder_name, 'Publishing/Client_Review')
path_9 = os.path.join(os.getcwd(), folder_name, 'Publishing/Delivery')
path_10 = os.path.join(os.getcwd(), folder_name, 'Publishing/PLLP')
path_11 = os.path.join(os.getcwd(), folder_name, 'Publishing/To_PM')
path_12 = os.path.join(os.getcwd(), folder_name, 'Publishing/To_PS')
path_13 = os.path.join(os.getcwd(), folder_name, 'Received/')
path_14 = os.path.join(os.getcwd(), folder_name, 'RFQ/')
path_15 = os.path.join(os.getcwd(), folder_name, 'Schedule/')
path_16 = os.path.join(os.getcwd(), folder_name, 'TM/')
path_17 = os.path.join(os.getcwd(), folder_name, 'To_Client/Final')
path_18 = os.path.join(os.getcwd(), folder_name, 'To_Client/Review')
path_19 = os.path.join(os.getcwd(), folder_name, 'To_PS/')

print("The current working directory is %s" % os.getcwd())

for path in [path_1, path_2, path_3, path_4, path_5, path_6, path_7, path_8, path_9, path_10, path_11, path_12, path_13, path_14, path_15, path_16, path_17, path_18, path_19]:    
    try: 
        os.makedirs(path)
    except OSError:
        print(f"Creation of the directory {path} failed")    
    else:
        print(f"Successfully created the directory {path}")
