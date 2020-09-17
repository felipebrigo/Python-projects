import pandas as pd
import json
import ast
import smtplib

newdictionary=[]
def add_file_txt():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj1.txt", "a",encoding="latin-1") as w, open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/Layout CNPJ e dados do governo/cnpj10.txt", "r", encoding="latin-1") as r:
        r=r.read()
        w.write(r)
        
def convertfile():
    newlist=[]
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj.txt","r",encoding="UTF-8",errors="replace") as r:
        dictionary=r.read()
        newdictionary=dictionary.replace("}","}$").split("$")
        print(len(newdictionary))
        for i in range(0,len(newdictionary)):
            test=ast.literal_eval(newdictionary[i])
            newlist.append(test)
        newdictionary=[]
        dictionary=""    
        dataframe=pd.DataFrame(newlist)
        print(dataframe)
        dataframe.to_csv(r'export_dataframe.csv')
        
        ''' print(newdictionarylist[i])        
        jsontext=json.loads(jsonlist)
        jsonitems=json.dumps(newdictionarylist[i])
        df=pd.read_json(jsonitems)
        print(df)
        for i in range (0,len(newdictionarylist)):
            if "/" in newdictionarylist[i][:5]:
                newdictionarylist.pop(i)
        print(len(newdictionarylist))
            jsontext=json.loads(data)
            newdictionary.append(jsontext)
            df=pd.DataFrame(dictionary)
            print(df)
        '''
        
        #df.to_excel(r'/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/testeexcel.xlsx')
        #print(df)
        
def testingfile():
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj-consolidado-filtrado.txt","r", encoding="UTF-8", errors="replace") as company:
        newcompany=company.read()
        pos=newcompany.find("BLUEQUEST",0,len(newcompany))
        print("Encontrado na linha " + str(pos))
        
def counting():
    newfile=[]
    with open("/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/cnpj-consolidado-filtrado.txt","r",encoding="utf-8",errors="replace") as file:
        file=file.read()
        newfile=file.split("{")
        print(len(newfile))
        for i in range (0,len(newfile)):
            if "BLUEQUEST" in newfile[i]:
                print(str(i))
                print(newfile[i])
                break

def email():
    import smtplib
    PARA = "comercial.leoma@gmail.com"      #e-mail destino
    USUARIO= "comercial.leoma.auto@gmail.com"      #seu  email no google
    SENHA= "comercial.leoma.auto2020"                  #sua senha no google
    
    ASSUNTO= "teste de envio de email via python\n"
    TEXTO= "Email enviado através de um programa python\n\n"
    
    print ("Enviando email")
    smtpserver= smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(USUARIO,SENHA)
    msg= "Testando Mensagem Automatica"
    
    smtpserver.sendmail(USUARIO,PARA,msg)
    smtpserver.quit() 
    print ("Email enviado")
    
print("Your program has been started!")
#add_file_txt()
#convertfile()
counting()
#testingfile()
#email()

print("Your program has been finished!")     