#PHOTO ORGANIZER
from PIL import Image
import os
import shutil

#Global variables declared or initialized
photo_files=[]
extentions=["jpg", "jpeg", "gif", "tiff"]

#Capture the path where the program will start to find out pics (from there onwards in all folders inside the path)
def path(path_start):
    files=os.listdir(path_start)
    for file in files:
        #file_split=file.split(".")
        if "JPG" in file.lower():
            photo_files.append(file)
print(photo_files)

#Capture all photo's data
def data_photo(path_start, photo_files):
    im=Image.open(path_start + photo_files[1])
    info=im._getexif()
    print(info)
    if 36867 in info:
        date=info[36867]
        print(date)
        date=dt.strptime(date,"%Y:%m:%d %H:%M:%S")
        print(date.strftime("%B"))
    else:
        print("Código não encontrado")
#--------------------------------
    
os.path.basename()    
os.path.join()

#Checkout if files are photos (.gif/.jpg/.jpeg/.raw)


#Creating specific folders and move pics inside them
path_end=os.path.join(path_start,pic_year,pic_month)
os.makedirs(path_end)
shutil.move(path_start,path_end)
#To move pointer inside the path and paste all photo's files
os.chdir(path_start, pic_year, pic_month)

#Main program
path_start=os.getcwd()
path(path_start)


#Generate a .txt report into workspace with from (path) to (new path) and size of the file
report={}
report.update{'filename - from - to - size'}
