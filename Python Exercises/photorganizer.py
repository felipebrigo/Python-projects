#PHOTO ORGANIZER
from PIL import Image
import os
import shutil

#Global variables declared or initialized
photo_files=[]
extentions=[".jpg", ".jpeg", ".gif", ".tiff"]
#Capture the path where the program will start to find out pics (from there onwards in all folders inside the path)
def path():
    path_start=os.getcwd()
    files=os.listdir(path_start)
    for file in files:
        file_split=file.split(".")
    if "jpeg" in file_split:
        photo_files.append(file)
print(photo_files)  

#--------------------------------
    
os.path.basename()    
os.path.join()

#Checkout if files are photos (.gif/.jpg/.jpeg/.raw)
#Capture all photo's data

#Creating specific folders and move pics inside them
path_end=os.path.join(path_start,pic_year,pic_month)
os.makedirs(path_end)
shutil.move(path_start,path_end)
#To move pointer inside the path and paste all photo's files
os.chdir(path_start, pic_year, pic_month)
#Generate a .txt report into workspace with from (path) to (new path) and size of the file
report={}
report.update{'filename - from - to - size'}
