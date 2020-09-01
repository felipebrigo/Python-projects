import pandas as pd
newdictionary=[]
def add_file_txt():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj1.txt", "a",encoding="latin-1") as w, open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj10.txt", "r", encoding="latin-1") as r:
        r=r.read()
        w.write(r)
        
def convertfile():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj.txt","r") as r:
        dictionary=r.readlines()
        for i in range(0,len(dictionary)):
            newdictionary.append(dictionary[i])
            #newdictionary = dictionary.replace('}\n','},')
        df=pd.DataFrame.from_dict(newdictionary,orient="columns")
        print(df)
        
print("Your program has been started!")
#add_file_txt()
convertfile()

print("Your program has been finished!")     