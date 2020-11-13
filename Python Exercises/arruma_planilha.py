import pandas as pd
import xlrd

excel = pd.read_excel('/Users/mac/Downloads/Clientes Fios e Cabos.xlsx', sheet_name='export_dataframe')
excel = excel.drop(labels='valor', axis=1)
excel = excel.drop(labels='contem', axis=1)
#excel = excel.drop(labels='index', axis=1)
list_to_exclude = ['AUTO', 'FORMA', 'TEXT', 'MOD', 'TECI', 'HIDRAU', 'ARMAR', 'MAL']
max_lim=len(excel.index)
spreadsheet_treated = excel.copy()
cont=0
for line in range (0,max_lim-cont):
    nome_empresa = spreadsheet_treated.iloc[line-cont,3]
    cnae = str(spreadsheet_treated.iloc[line-cont,6])
    if cnae[:1] == '1' or cnae[:1] == '9' or cnae[:1] == '8' or cnae[:1] == '7':
        spreadsheet_treated = spreadsheet_treated.drop(line)
        cont = cont + 1
    else:
        for text_to_exclude in range(0,len(list_to_exclude)):
            if list_to_exclude[text_to_exclude] in nome_empresa:
                spreadsheet_treated = spreadsheet_treated.drop(line)
                cont = cont + 1
                break
spreadsheet_treated.to_csv(r'/Users/mac/Documents/Lista FCA Leandro/CNPJ empresas/export_dataframe_treated.csv')
