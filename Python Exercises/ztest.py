import pandas as pd
import json
import ast

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
    import imghdr
    from email.message import EmailMessage
    msg=EmailMessage()
    para=[] #e-mail destino
    user= "comercial.leoma.auto@gmail.com"      #seu  email no google
    password= "comercial.leoma.auto2020"                  #sua senha no google
    
    string="Boa tarde./nSou Felipe Brigo, gerente comercial da Leoma Auto Partes, representante da \033[14;31mMOPAR\033[m, braço de vendas do grupo \033[14;31mFIAT/JEEP/CHRYSLER – FCA\033[m./n/nVenho com este email oferecer nossos serviços e as incríveis ofertas que temos disponíveis em nossa linha. São peças \033[14;31m100% ORIGINAIS, COM PREÇOS BEM REDUZIDOS E ATRATIVOS\033[m e com \033[14;31mTODA GARANTIA FCA QUE SEU CLIENTE DESEJA\033[m, faturadas diretamente da \033[14;31mFIAT\033[m e suas concessionárias com entrega especial para você, nosso cliente!/n/nSegue abaixo alguns exemplos de nossas ofertas:"
    
    print ("Enviando email")
    with open("/Users/mac/Documents/Lista FCA Leandro/email-list.txt",'r') as f:
        mailto=f.readlines()
        
    msg.set_content(string)
    msg['From']=user
    msg['To']=para
    msg['Subject']="LEOMA - OPORTUNIDADE DE PEÇAS FIAT/CHRYSLER/JEEP - Normal"
    try:
        smtpserver= smtplib.SMTP("smtp.gmail.com",25)
        smtpserver.connect("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(user,password)
        #smtpserver.sendmail(USUARIO,PARA,msg)
        file="/Users/mac/Downloads/Captura de Tela 2020-09-22 às 14.01.00 (2).png"
        with open(file, 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',subtype=imghdr.what(None, img_data))
        smtpserver.send_message(msg)
    except Exception as e:
        with open ("Errors.txt",mode="a") as errorlist:
            errorlist.writelines(e)
    finally:
        smtpserver.quit() 
    print ("Email enviado")
    
print("Your program has been started!")
#add_file_txt()
#convertfile()
#counting()
#testingfile()
email()

print("Your program has been finished!")     