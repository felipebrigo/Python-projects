import os
from PIL import Image
from datetime import datetime as dt
from time import time,ctime

'''teste='/Users/mac/Downloads'
os.chdir(teste)
teste2=teste+'/Python'+'/teste'+'/teste2'
os.makedirs(teste2)
print(os.getcwd())
photo_files=[]
extentions=(".jpg", ".jpeg", ".gif", ".tiff")
#print(os.path.getsize('/Users/mac/Downloads/Lista Esquadrias'))
print(os.listdir('/Users/mac/Downloads'))
files=os.listdir("/Users/mac/Downloads")
for file in files:
    #file_split=file.split(".")
    for a in range (0,len(extentions)):
        if extentions[a] in file.lower():
            photo_files.append(file)
print(photo_files)       

im=Image.open("/Users/mac/Downloads/" + "Petra Metais.jpeg")
info=im._getexif()
print(info)
if 36867 in info:
    date=info[36867]
    print(date)
    date=dt.strptime(date,"%Y:%m:%d %H:%M:%S")
    print(date.strftime("%B"))
else:
    print("Código não encontrado")
    print(info.values[:])
'''    
photo="/Users/mac/Downloads/oficina-de-inverno-aplicativos-de-edicao-de-fotos-por-do-sol.jpg"
complete_date=os.path.getmtime(photo)
complete_date=ctime(complete_date)
date_strip=dt.strptime(complete_date,"%a %b %d %H:%M:%S %Y")
month=date_strip.strftime("%B")
year=date_strip.strftime("%Y")
general_data=os.path.join(photo,year,month)
print(general_data)