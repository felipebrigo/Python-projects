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
    year_list={}
    for year_list in complete_data_list:
        #for y_list in year_list.values():
            #file_directory=os.path.basename(complete_data_list[year_list]["Original_Path"])
        path_year=year_list["Year"]
        path_month=year_list["Month"]
        if not path_year in year:
            year.append(path_year)
        if not path_month in month:
            month.append(path_month)

    year.sort()
    month.sort()    
    print(year)
    print(month)
    
    for new_file in complete_data_list:
        try:
            os.makedirs(new_file["Path_End"])
        except:
            break
'''        
    for new_year_list in complete_data_list:
        for y in year:
            folder_name=os.path.join(new_year_list["Original_Path"],y)
            os.makedirs(folder_name)
        for m in month:
            os.makedirs(m)'''

#Move files from Original_Path to Path_End        
def move_file():
    for moving in complete_data_list:
        shutil.move(complete_data_list["Original_Path"], complete_data_list["Path_End"])

#Main program
path_start='/Users/mac/Downloads'
#os.getcwd()
path(path_start)
data_photo(path_start, photo_files)
create_folder()
move_file()

print(complete_data_list)
#Generate a .txt report into workspace with from (path) to (new path) and size of the file
#report={}
#report.update{'filename - from - to - size'}
