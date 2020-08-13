#PHOTO ORGANIZER
from PIL import Image
import os
import shutil
import collections
from datetime import datetime as dt
import csv
from time import time,ctime

class photOrganizer:
    
    #Global variables declared/initialized
    complete_data_list=[]
    photo_files=[]   
    extentions=["jpg", "jpeg", "gif", "tiff", "raw"] 

    #Capture all files in the main path where the program will start to find out pics
    def path(self,path_start):
        global photo_files
        files=os.listdir(path_start)
        for file in files:
            for a in range (0,len(self.extentions)):
                if self.extentions[a] in file.lower():
                    self.photo_files.append(file)

    #Capture all photo's data and put on a list
    def data_photo(self,path_start, photo_files):
        #Variables declared
        general_data={}
        year=[]
        month=[]
        global complete_data_list

        for b in range(0,len(self.photo_files)):
            im=Image.open(os.path.join(path_start, self.photo_files[b]))
            info=im._getexif()
            try:
                
                if 36867 in info:
                    complete_date=info[36867]
                    date_strip=dt.strptime(complete_date,"%Y:%m:%d %H:%M:%S")
                    month=date_strip.strftime("%B")
                    year=date_strip.strftime("%Y")
                    general_data["Original_Path"]=path_start
                    general_data["File"]=self.photo_files[b]
                    general_data["Year"]=year
                    general_data["Month"]=month
                    general_data["Path_End"]=os.path.join(self.path_start, year, month)
                    self.complete_data_list.append(general_data.copy())
                else:
                    complete_date=os.path.getmtime(os.path.join(self.path_start,self.photo_files[b]))
                    complete_date=ctime(complete_date)
                    date_strip=dt.strptime(complete_date,"%a %b %d %H:%M:%S %Y")
                    month=date_strip.strftime("%B")
                    year=date_strip.strftime("%Y")
                    general_data["Original_Path"]=self.path_start
                    general_data["File"]=self.photo_files[b]
                    general_data["Year"]=year
                    general_data["Month"]=month
                    general_data["Path_End"]=os.path.join(self.path_start,year,month)
                    self.complete_data_list.append(general_data.copy())
                    
            except:
                    general_data["Original_Path"]=self.path_start
                    general_data["File"]=self.photo_files[b]
                    general_data["Year"]="No_Data"
                    general_data["Month"]="No_Data"
                    general_data["Path_End"]=os.path.join(self.path_start,"No_Data", "No_Data")
                    self.complete_data_list.append(general_data.copy())

    #Creating specific folders and subfolders
    def create_folder(self):
        err=[]
        for new_file in self.complete_data_list:
            try:
                os.makedirs(new_file["Path_End"])
            except:
                err.append(Exception.__class__)            
        return err

    #Moving files from Original_Path to Path_End        
    def move_files(self):
        error_moving=[]
        for moving in self.complete_data_list:
            try:
                shutil.move(os.path.join(moving["Original_Path"],moving["File"]), os.path.join(moving["Path_End"],moving["File"]))
            except:
                error_moving.append(Exception.__class__)
        return error_moving
                
    #Generate a .csv report into workspace with last path and new path
    def report(self):
        complete_data_dict=dict
        try:
            complete_data_dict=self.complete_data_list[0]  
        except:
            complete_data_dict={""}
        with open('photo_organizer.csv', 'w', newline='') as file:
            fieldnames=complete_data_dict
            writer = csv.DictWriter(file, fieldnames=fieldnames, restval="")
            writer.writeheader()
            for data in self.complete_data_list:
                writer.writerow(data)        
                
    #Main Program    
    def program(self):
        self.path_start='/Users/mac/Downloads'
        #self.path_start=os.getcwd()
        self.path(self.path_start)
        self.data_photo(self.path_start, self.photo_files)
        create_error=self.create_folder()
        moving_errors=self.move_files()
        self.report()

PO=photOrganizer()
PO.program()