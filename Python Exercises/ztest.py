import os
from PIL import Image
from datetime import datetime as dt

'''teste='/Users/mac/Downloads'
os.chdir(teste)
teste2=teste+'/Python'+'/teste'+'/teste2'
os.makedirs(teste2)
print(os.getcwd())'''
photo_files=[]
extentions=(".jpg", ".jpeg", ".gif", ".tiff")
#print(os.path.getsize('/Users/mac/Downloads/Lista Esquadrias'))
print(os.listdir('/Users/mac/Downloads'))
files=os.listdir("/Users/mac/Downloads")
for file in files:
    file_split=file.split(".")
    if "JPG" in file_split:
        photo_files.append(file)
print(photo_files)        

im=Image.open("/Users/mac/Downloads/" + photo_files[1])
info=im._getexif()
print(info)
if 36867 in info:
    date=info[36867]
    date=dt.strptime(date,"%Y:%m:%d")
    print(date.strftime("%B"))
else:
    print("Código não encontrado")
    print(info.values[:])