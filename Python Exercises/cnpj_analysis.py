#import timeit
import pandas as pd
from timeit import default_timer as timer
import os

textsliced=[]
data_cnpj_list=[]
data_company_dict={}
pathfile="/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/K3241.K03200DV.D00703.L00020.txt"
endfilenbr=20

#Slicing the whole datafile in 1200 characters each time and filter only 
#companies who is active (in operation)
def slicing():
    global textsliced
    company_active=[]
    with open(pathfile, "r",encoding="UTF-8",errors="replace") as r:
        textsliced=r.readlines()
        #textsliced=[r[i:(i+1201)] for i in range(0, len(r),1201)]
        for item in range(0,len(textsliced)):
            if textsliced[item][0]=='1':
                if textsliced[item][223:225]=='02':
                    company_active.append(textsliced[item])
        with open(str("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj" + str(endfilenbr) + ".txt"),"w") as file:
            for j in range (0,len(company_active)):
                file.writelines(str(company_active[j]))

def openfile(programnumber):
    global textsliced
    with open(str("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj" + str(programnumber) + ".txt"), "r",encoding="UTF-8",errors="replace") as r:
        textsliced=r.readlines()
        #textsliced=[r[i:(i+1201)] for i in range(0, len(r), 1201)]

def file_type():
    global textsliced
    #companies=["AUTO","MECANICA","SUSPEN","VEICU","BLUEQUEST","PECAS","PNEU", "RECAPA"]
    companies=["FIO", "CABOS", "CONDUTOR"]
    state=["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    for item in range(0,len(textsliced)):
        if textsliced[item][682:684] in state:
            for item_companies in range(0,len(companies)):
                if companies[item_companies] in textsliced[item][18:223]:
                    data_cnpj(textsliced[item])

#Company treatment - 1200 characters    
def data_cnpj(text):
    data_company_dict={"cnpj":str(text[3:17]).strip(), 
                       "unid":str(text[17:18]).strip(),
                       "razaosocial":(str(text[18:168]).replace("'","-")).strip(),
                       "nomefantasia":(str(text[168:223]).replace("'","-")).strip(),
                       "inicioatividade":str(text[367:375]).strip(),
                       "cnaeprincipal":str(text[375:382]).strip(),
                       "tipoendereco":str(text[382:402]).strip(),
                       "endereco":(str(text[402:462]).replace("'","-")).strip(),
                       "numero":str(text[462:468]).strip(),
                       "complemento":str(text[468:624]).strip(),
                       "bairro":(str(text[624:674]).replace("'","-")).strip(),
                       "cep":str(text[674:682]).strip(),
                       "uf":str(text[682:684]).strip(),
                       "cidade":(str(text[688:738]).replace("'","-")).strip(),
                       "telefone1":str(text[738:750]).strip(),
                       "telefone2":str(text[750:762]).strip(),
                       "email":str(text[774:889]).strip(),
                       "capitalsocial":str(text[891:905]).strip(),
                       "porteempresa":str(text[905:907]).strip()}
    data_cnpj_list.append(data_company_dict.copy())

def pandas_dataframe():
    
    global data_cnpj_list
    df=pd.DataFrame(data_cnpj_list)
    print(df)
    df.to_csv(r'/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/export_dataframe.csv')
    
    
#Export to csv file
def write_txt_file():
    print(len(data_cnpj_list))
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj-consolidado-filtrado.txt","a", newline="") as cnpj:
        for j in range (0,len(data_cnpj_list)):
            cnpj.writelines(str(data_cnpj_list[j]))
     
#Main
def mainprogram():
    #slicing() 
    for programnumber in range(1,(endfilenbr+1)):
        openfile(programnumber)
        file_type()

print("Your program has been started!")        
start = timer()
mainprogram()
write_txt_file()
pandas_dataframe()
end = timer()
print(end - start)
print("Your program has been concluded successfully!")