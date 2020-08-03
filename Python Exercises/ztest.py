import os
from PIL import Image
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
    if "jpeg" in file_split:
        photo_files.append(file)
print(photo_files)        

'''im=Image.open('/Users/mac/Downloads/WhatsApp Image 2019-12-11 at 15.41.34.jpeg')
info=im._getexif()
if 36867 in info:
    date=info[36867]
    print(date)
else:
print("Código não encontrado")
print(info.values[:])'''
