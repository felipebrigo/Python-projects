#import timeit
from timeit import default_timer as timer
start = timer()
textsliced=[]
data_cnpj_list=[]

#Slicing the whole datafile in 1200 characters each time
def slicing():
    print("Your program has been started!")
    global textsliced
                    
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/K3241.K03200DV.D00703.L00010.txt", "r",encoding="latin-1") as r:
        r=r.read()
        textsliced=[r[i:i+1200] for i in range(0, len(r), 1201)]

def file_type():
    global textsliced
    state=["PR","SC","RS"]
    for item in range(0,len(textsliced)):
        if textsliced[item][0]=='1':
            if textsliced[item][223:225]=='02':
                if textsliced[item][682:684] in state:
                    data_cnpj(textsliced[item])

#Company treatment - 1200 characters    
def data_cnpj(text):
    data_cnpj_list.append(text)

#Export to csv file
def write_txt_file():
    with open("cnpj.txt","w") as cnpjteste:
        cnpjteste.writelines(data_cnpj_list)
        
#Main
slicing()
file_type()
write_txt_file()
end = timer()
print(len(textsliced))
print(end - start)
print("Your program has been concluded successfully!")

#print(timeit.timeit(slicing, number=1))

'''Using Buffer on Slicing() is too Slow (0.06865)
buffersize = 1000000
buffer = []
i=0
with open("/Users/mac/Documents/Lista FCA Leandro/Teste-layout.txt", "r") as r, open("teste.txt", "w") as w:
    r=r.read()
    for text in r:
        text=r[i:i+1200]
        i+=1200
        buffer.append(text)
        if len(buffer) > buffersize:
            w.writelines(buffer)
            buffer = []
    w.writelines(buffer)'''