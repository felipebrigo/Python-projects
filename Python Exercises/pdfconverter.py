import os
import PyPDF2
import re
import pandas as pd


paths=[]
data_list=[]

def filename():
    paths=os.listdir('/Users/mac/Documents/Leoma-Bluequest/Alfieri-UBC Novelis/EXPORTAÇÃO UBC/ForteLigas/')
    #paths.append('TICKET  NF-13063.pdf')
    indice=-1
    for path in paths:
        indice+=1
        if not path.endswith('pdf'):
            paths.pop(indice)
    return paths


def readpdf(paths):
    
    for path in paths:
        # creating a pdf file object 
        pdfFileObj = open('/Users/mac/Documents/Leoma-Bluequest/Alfieri-UBC Novelis/EXPORTAÇÃO UBC/ForteLigas/'+ path, 'rb') 
        
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)         
        
        # creating a page object 
        pageObj = pdfReader.getPage(0) 

        # extracting text from page 
        pageObjtext=pageObj.extractText()
        Objtext=re.split('  ',pageObjtext)
        
        # closing the pdf file object 
        pdfFileObj.close() 
        
        '''
        Objtextindex=-1
        for item in Objtext:
            Objtextindex+=1
            if Objtext[Objtextindex]!='':
                print(str(Objtextindex) + ' - ' + item)
        '''     
        
        dados_dict={
        'Arquivo':[path],    
        'descricao':[Objtext[604]],
        'peso_bruto':[Objtext[610]],
        'tara':[Objtext[611]],
        'peso_liquido':[Objtext[615]],
        'preco':[Objtext[617]],
        'pacotes':[Objtext[635]],
        'motorista':[Objtext[906]],
        'placa':[Objtext[964]],
        'nf':[Objtext[1113]],
        'container':[Objtext[1173]],
        'lacre':[Objtext[1173]],
        'tara_container':[Objtext[1174]],
        'placa carreta':[Objtext[1354]],
        }
    
        data_list.append(dados_dict)
        
        
    return data_list
        
    '''
        # printing number of pages in pdf file 
        number_of_pages = pdfReader.getNumPages()
        print(number_of_pages)
        
        parsed = ''.join(page_content)

        print("Sem eliminar as quebras")
        print(parsed)

        # remove as quebras de linha
        parsed = re.sub('\n', '', parsed)
        print("Após eliminar as quebras")
        print(parsed)

        print("\nPegando apenas as 20 primeiras posições")
        novastring = parsed[0:20]
        print(novastring)
    '''

items=filename()
data_list=readpdf(items)
data=pd.DataFrame(data_list)
print (data)
data.to_csv(r'/Users/mac/Documents/Leoma-Bluequest/Alfieri-UBC Novelis/EXPORTAÇÃO UBC/ForteLigas/export_dataframe.csv')
print ('Processo Concluido')


