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
    #para=[] e-mail destino
    user= "comercial.leoma.auto@gmail.com"      #seu  email no google
    password= "comercial.leoma.auto2020"                  #sua senha no google
    
    string1="""Boa tarde.\n
Meu nome é Felipe Brigo e sou gerente comercial da Leoma Repr. Auto Peças, representante da MOPAR, braço de pós-vendas do grupo FIAT/JEEP/CHRYSLER – FCA.
    
Venho com este email oferecer nossos serviços e as incríveis ofertas que temos disponíveis em nossa linha. São peças 100% ORIGINAIS, COM PREÇOS BEM REDUZIDOS E ATRATIVOS e com TODA GARANTIA FCA QUE SEU CLIENTE DESEJA, faturadas diretamente da FIAT e suas concessionárias com entrega especial para você, nosso cliente!
    
Segue abaixo alguns exemplos de nossas ofertas:\n
MANUTENÇÃO PREVENTIVA:
Número Fiat 51917747 - FILTRO DE AR COMPLETO STRADA ----------------------- R$ 111,16
Número Fiat 7724422  - FILTRO COMBUSTIVEL RETENCAO PARTICULAS UNO/FIORINO - R$ 52,34
Número Fiat 46807203 - FILTRO DE AR COMPLETO STILO ------------------------ R$ 44,24
Número Fiat 46833535 - FILTRO DE AR COMPLETO DOBLÒ ------------------------ R$ 107,47
Número Fiat 51977572 - FILTRO DE AR COMPLETO RENEGADE/COMPASS (2015 -> ) -- R$ 199,06
Número Fiat 7091228  - FILTRO DE AR COMPLETO SERV. PES. DOBLÒ (2002-2009) - R$ 37,98
Número Fiat 46805832 - FILTRO OLEO PALIO FASE 1/2 ------------------------- R$ 6,59
Número Fiat 46816929 - SENSOR ABS RODAS TRASEIRAS STILO (2003-2007) ------- R$ 9,11
Número Fiat 55238304 - FILTRO OLEO STRADA/PALIO FASE 3 -------------------- R$ 18,23
    
ACESSÓRIOS:
Número Fiat 7084241     - ALTO FALANTE 6 POL. TRIAX. 40W PARA STRADA (2001-2013) - R$ 18,60
Número Fiat 7086704     - KIT RADIO CD MP3 PRATA LUXOR PARA PUNTO ---------------- R$ 372,94
Número Fiat 7083595     - KIT RODAS LIGA LEVE 16POL STILO ------------------------ R$ 640,01
Número Fiat 100216484   - RADIO CD BLACK PIANO IL803 ----------------------------- R$ 302,03
Número Fiat 100231999   - RADIO USB BLUETOOTH ------------------------------------ R$ 529,10
Número Fiat K1AN31PAKAD - RODA DE ALUMINIO 16POL FREEMONT ------------------------ R$ 324,45
Número Fiat 7087418     - RODA EM LIGA LEVE 17POL JOGO TJET PUNTO ---------------- R$ 881,87
Número Fiat 7086910     - RODA EM LIGA LEVE ARO 15POL JOGO SIENA HLX (2008-2012) - R$ 1.139,39

MAIORES OPORTUNIDADES:
Número Fiat 51769407 - ALTERNADOR DENSO 70A PALIO/STRADA ------------------------------ R$ 139,94
Número Fiat 50038663 - BLOCO MOTOR COM PISTOES E ANEIS PARA LINEA 1.9 16V (2009-2014) - R$ 261,37
Número Fiat 46422591 - BOMBA DIRECAO HIDRAULICA	UNO/FIORINO --------------------------- R$ 205,78
Número Fiat 71739488 - CABECOTE COM VALVULAS PARA STRADA 1.3 8V CF2/BZ COM FURO M16 --- R$ 412,06
Número Fiat 51846264 - CENTRAL ELETR IGNICAO INJECAO MARELLI PARA PUNTO --------------- R$ 360,67
Número Fiat 55212349 - CENTRAL ELETR IGNICAO INJECAO MARELLI PARA STRADA -------------- R$ 272,69
Número Fiat 7087935  - CENTRAL ELETRON IGNICAO INJECAO DELPHI PARA IDEA --------------- R$ 24,00
Número Fiat 55208474 - EIXO COMANDO VALVULAS ADMISSAO PARA PUNTO/LINEA/BRAVO ---------- R$ 198,71
Número Fiat 50011322 - RADIADOR ARREFECIMENTO MOTOR UNO/FIORINO ----------------------- R$ 390,85
Número Fiat 46530592 - TURBOCOMPRESSOR GARRET ----------------------------------------- R$ 84,45

    
Temos mais de 50.000 itens, desde parafusos e arruelas até laterais inteiras, câmbios e motores completos, com preços bem reduzidos, porém estoques limitados. Entre em contato conosco respondendo este email e/ou enviando uma mensagem para nosso Whatsapp – (11) 99709-5397 e mencionando a linha de produtos a qual trabalha para receber uma lista personalizada de todos nossos itens disponíveis e valores (Manutenção preventiva, Elétrica, Suspensão, Borracharia/Rodas, Injeção, Motor, etc).
     
Esperamos poder ajudar sua empresa a oferecer produtos originais e de altíssima qualidade a seus clientes, com custo totalmente acessível e compatível com o mercado.\n
 
Boa sorte e bons negócios.\n

Atenciosamente\n

Felipe Brigo
Leoma Auto Repres. Com. E Consultoria 
Cel/Whatsapp 55 11 99709-5397
comercial.leoma.auto@gmail.com
    
"""
    
    print ("Enviando email")
    with open("/Users/mac/Documents/Lista FCA Leandro/email-list.txt",'r') as f:
        mailto=f.readlines()
        
    msg.set_content(string1)
    msg['From']=user
    msg['Subject']="LEOMA - OPORTUNIDADE DE PEÇAS FIAT/CHRYSLER/JEEP"
    try:
        smtpserver=smtplib.SMTP("smtp.gmail.com",25)
        smtpserver.connect("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(user,password)
        file="/Users/mac/Downloads/Captura de Tela 2020-09-22 às 14.01.00 (2).png"
        with open(file, 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',subtype=imghdr.what(None, img_data))
        msg['To']="comercial.leoma@gmail.com"
        for para in range(453,len(mailto)):
            smtpserver.send_message(msg)
            msg.replace_header('To',mailto[para])
            
    except Exception as e:
        with open ("Errors.txt",mode="a") as errorlist:
            errorlist.writelines(e.args())
    finally:
        smtpserver.quit() 
   
print("Your program has been started!")
#add_file_txt()
#convertfile()
#counting()
#testingfile()
email()

print("Your program has been finished!")     