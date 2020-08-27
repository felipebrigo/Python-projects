#import timeit
from timeit import default_timer as timer
start = timer()
textsliced=[]
data_company_list=[]

#Slicing the whole datafile in 1200 characters each time
def slicing():
    print("Your program has been started!")
    global textsliced
                    
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/consolidado.txt", "r",encoding="latin-1") as r:
        r=r.read()
        textsliced=[r[i:i+1200] for i in range(0, len(r), 1201)]

def file_type():
    global textsliced
    companies=["AUTO","MECANICA","SUSPEN"]
    for item in range(0,len(textsliced)):
        for item_companies in range(0,len(companies)):
            if companies[item_companies] in textsliced[item][18:223]:
                data_company(textsliced[item])

#Company treatment - 1200 characters    
def data_company(text):
    
    data_company_list.append(text)

#Export to csv file
def write_txt_file():
    with open("company.txt","w") as company:
        company.writelines(data_company_list)
        
#Main
slicing()
file_type()
write_txt_file()
end = timer()
print(len(textsliced))
print(end - start)
print("Your program has been concluded successfully!")