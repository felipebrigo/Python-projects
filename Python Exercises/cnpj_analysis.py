#import timeit
from timeit import default_timer as timer
start = timer()
textsliced=[]
#header_treatment_list=[]
data_cnpj_list=[]
#partner_list=[]
#secondary_list=[]
#trailler_list=[]

#Colocar timming de qto tempo o programa está rodando
#Colocar % de dado concluido

#Slicing the whole datafile in 1200 characters each time
def slicing():
    global textsliced
                    
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/K3241.K03200DV.D00703.L00001.txt", "r",encoding="latin-1") as r:
        r=r.read()
        textsliced=[r[i:i+1200] for i in range(0, len(r), 1201)]

def file_type():
    global textsliced
    state=["PR","SC","RS"]
    for item in range(0,len(textsliced)):
        if textsliced[item][0]=='1':
            if textsliced[item][224:226]=='02':
                if textsliced[item][683:685] in state:
                    data_cnpj(str(item) + " - " + textsliced[item])
        '''    
        elif textsliced[item][0]=='2':
            partner(str(item) + " - " + textsliced[item])
            
        elif textsliced[item][0]=='6':
            secondary(str(item) + " - " + textsliced[item])
            
        elif textsliced[item][0]=='9':
            trailler(str(item) + " - " + textsliced[item])
        '''
'''Header treatment - 1200 characteres
def header_treatment(text):
    header_treatment_list.append(text)
'''
#Company treatment - 1200 characters    
def data_cnpj(text):
    data_cnpj_list.append(text)
    

'''Partners treatment - 1200 characters
def partner(text):
    partner_list.append(text)

#Secondary CNAE
def secondary(text):
    secondary_list.append(text)
    
#Trailler
def trailler(text):
    trailler_list.append(text)
'''
#Export to csv file
def write_txt_file():
    with open("cnpj.txt","w") as cnpjteste:
        cnpjteste.writelines(data_cnpj_list)
    '''with open("partner.txt","w") as partnerlist:
        partnerlist.writelines(partner_list)'''
        
#Main
slicing()
file_type()
write_txt_file()
end = timer()
print(len(textsliced))
print(end - start)
print("Your program has been concluded successfully!")

#Import Pandas to re-arrange all list    
#print(timeit.timeit(slicing, number=1))
#print(timeit.timeit(file_type, number=1))

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