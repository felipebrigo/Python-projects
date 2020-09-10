import pandas as pd
import json

newdictionary=[]
def add_file_txt():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj1.txt", "a",encoding="latin-1") as w, open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj10.txt", "r", encoding="latin-1") as r:
        r=r.read()
        w.write(r)
        
def convertfile():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj.txt","r",encoding="UTF-8",errors="replace") as r:
        dictionary=r.readlines()
        for i in range(0,len(dictionary)):
            data=dictionary[i]
            data=data.replace("'",'"')
            jsontext=json.loads(data)
            newdictionary.append(jsontext)
            #newdictionary = dictionary.replace('}\n','},')
            #df=pd.DataFrame(dictionary)
            #print(df)
        df=pd.DataFrame(newdictionary)
        df.to_excel(r'/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/testeexcel.xlsx')
        #print(df)
        
def counting():
    endfilenbr=1
    slicedtext=0
    path='K3241.K03200DV.D00703.L00001'
    with open(str("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/" + "cnpj111" + ".txt"),"r",encoding="utf-8",errors="replace") as file:
        newfiletext=file.readlines()
        for i in range(0,len(newfiletext)):
            slicedtext=slicedtext+len(newfiletext[i])
            print(str(newfiletext[i]))
        print(len(newfiletext))
        print(slicedtext)
        print(slicedtext,end='\n')
        '''
        for j in range (0,len(company_active)):
            file.writelines(str(company_active[j]))
        '''
        
print("Your program has been started!")
#add_file_txt()
convertfile()
#counting()

print("Your program has been finished!")     