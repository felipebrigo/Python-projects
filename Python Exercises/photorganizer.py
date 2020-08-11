#PHOTO ORGANIZER
from PIL import Image
import os
import shutil
import collections
from datetime import datetime as dt

#Global variables declared or initialized
general_data={}
complete_data_list=[]
photo_files=[]
folder_list=[]
year=[]
month=[]
extentions=["jpg", "jpeg", "gif", "tiff", "raw"]
err=[]
error_moving=[]

#Capture all files in the main path where the program will start to find out pics
def path(path_start):
    global folder_list, photo_files
    files=os.listdir(path_start)
    for file in files:
        if not "." in file:
            folder_list.append(file)
        for a in range (0,len(extentions)):
            if extentions[a] in file.lower():
                photo_files.append(file)
    print(photo_files)

#Capture all photo's data and put on a list
def data_photo(path_start, photo_files):
    global complete_data_list
    for b in range(0,len(photo_files)):
        im=Image.open(os.path.join(path_start, photo_files[b]))
        info=im._getexif()
        try:
            
            if 36867 in info:
                complete_date=info[36867]
                date_strip=dt.strptime(complete_date,"%Y:%m:%d %H:%M:%S")
                month=date_strip.strftime("%B")
                year=date_strip.strftime("%Y")
                general_data["Original_Path"]=path_start
                general_data["File"]=photo_files[b]
                general_data["Year"]=year
                general_data["Month"]=month
                general_data["Path_End"]=os.path.join(path_start, year, month)
                complete_data_list.append(general_data.copy())
            else:
                general_data["Original_Path"]=path_start
                general_data["File"]=photo_files[b]
                general_data["Year"]="No_Data"
                general_data["Month"]="No_Data"
                general_data["Path_End"]=os.path.join(path_start,"No_Data", "No_Data")
                complete_data_list.append(general_data.copy())
                
        except:
                general_data["Original_Path"]=path_start
                general_data["File"]=photo_files[b]
                general_data["Year"]="No_Data"
                general_data["Month"]="No_Data"
                general_data["Path_End"]=os.path.join(path_start,"No_Data", "No_Data")
                complete_data_list.append(general_data.copy())

#--------------------------------

#Creating specific folders and subfolders
def create_folder():
    for new_file in complete_data_list:
        try:
            os.makedirs(new_file["Path_End"])
        except:
            err.append(Exception.__class__)            
    #return err

#Moving files from Original_Path to Path_End        
#def move_files():
    for moving in complete_data_list:
        try:
            shutil.move(os.path.join(moving["Original_Path"],moving["File"]), os.path.join(moving["Path_End"],moving["File"]))
        except:
            error_moving.append(Exception.__class__)        
    return err

#Main program
path_start='/Users/mac/Downloads'
#os.getcwd()
path(path_start)
data_photo(path_start, photo_files)
create_error=create_folder()
print(error_moving)

print(complete_data_list)
#Generate a .txt report into workspace with from (path) to (new path) and size of the file
#report={}
#report.update{'filename - from - to - size'}
