#import timeit
from timeit import default_timer as timer
import pandas as pd
start = timer()
textsliced=[]
data_company_dict={}
data_company_list=[]

#Slicing the whole datafile in 1200 characters each time
def slicing():
    print("Your program has been started!")
    global textsliced
                    
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/consolidado.txt", "r",encoding="latin-1") as r:
        r=r.read()
        textsliced=[r[i+5:i+1200] for i in range(0, len(r), 1200)]

def file_type():
    global textsliced
    companies=["AUTO","MECANICA","SUSPEN"]
    for item in range(0,len(textsliced)):
        for item_companies in range(0,len(companies)):
            if companies[item_companies] in textsliced[item][18:223]:
                data_company(textsliced[item])

#Company treatment - 1200 characters    
def data_company(text):
    data_company_dict={'cnpj':str(text[3:17]).strip(), 
                       'unid':str(text[17:18]).strip(),
                       'razaosocial':str(text[18:168]).strip(),
                       'nomefantasia':str(text[168:223]).strip(),
                       'inicioatividade':str(text[367:375]).strip(),
                       'cnaeprincipal':str(text[375:382]).strip(),
                       'tipoendereco':str(text[382:402]).strip(),
                       'endereco':str(text[402:462]).strip(),
                       'numero':str(text[462:468]).strip(),
                       'complemento':str(text[468:624]).strip(),
                       'bairro':str(text[624:674]).strip(),
                       'cep':str(text[674:682]).strip(),
                       'uf':str(text[682:684]).strip(),
                       'cidade':str(text[688:738]).strip(),
                       'telefone1':str(text[738:750]).strip(),
                       'telefone2':str(text[750:762]).strip(),
                       'email':str(text[774:889]).strip(),
                       'capitalsocial':str(text[891:905]).strip(),
                       'porteempresa':str(text[905:907]).strip()}
        
    data_company_list.append(data_company_dict.copy())

#Export to csv file
def write_txt_file():
    with open("company.txt","w") as company:
        company.write(data_company_list)
        
#Main
slicing()
file_type()
#write_txt_file()
df=pd.DataFrame(data_company_list)
print(df)
df.to_csv(r'company.txt', mode='a')
end = timer()
print(len(textsliced))
print(end - start)
print("Your program has been concluded successfully!")