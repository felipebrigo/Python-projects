from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
from itertools import combinations
import os
import time

def load_file():
    result_df = pd.read_csv("megasena.csv", sep=";")
    result_df = result_df.rename_axis('index').reset_index()
    print(result_df)
    return result_df

def frequencies_of_ball(result_df, qty_games):
    if os.path.isfile('tmp_data.csv'):
        os.remove('tmp_data.csv')
    with open("tmp_data.csv", "a") as file:        
        for i in range(1, 7):
            bola1 = 'Bola' + str(i)
            result1 = pd.DataFrame(result_df.groupby([bola1])['index'].nunique())
            result1.to_csv(file)
    final_result = pd.read_csv("tmp_data.csv")
    df_remove = final_result.loc[(final_result['index'] == 'index')]
    final_df = final_result.drop(df_remove.index, axis=0).reset_index(drop=True)
    final_df = final_df.rename_axis('index1').reset_index()
    final_df['index'] = pd.to_numeric(final_df['index'])
    frequency = pd.DataFrame(final_df.groupby(['Bola1'])['index'].sum())
    frequency = frequency.sort_values(by=['index'], ascending=False)
    frequency['probability'] = (frequency["index"] / qty_games)
    os.remove('tmp_data.csv')
    with open("tmp_data.csv", "w") as file:
        frequency.to_csv(file)
    return frequency

def double_balls_combination(result_df, qty_games): 
    if os.path.isfile('tmp_data_2.csv'):
        os.remove('tmp_data_2.csv')
        
    with open("tmp_data_2.csv", "a") as file:        
        for i in range(1, 6):
            bola1 = 'Bola' + str(i)
            for j in range(i+1, 7):
                bola2 = 'Bola' + str(j)
                if i != j:
                    result1 = pd.DataFrame(result_df.groupby([bola1, bola2])['index'].nunique())
                    result1.to_csv(file)
                    
    final_result = pd.read_csv("tmp_data_2.csv")
    df_remove = final_result.loc[(final_result['index'] == 'index')]
    final_df = final_result.drop(df_remove.index, axis=0).reset_index(drop=True)
    final_df = final_df.rename_axis('index1').reset_index()
    final_df['index'] = pd.to_numeric(final_df['index'])
    frequency_2 = pd.DataFrame(final_df.groupby(['Bola1', 'Bola2'])['index'].sum())
    frequency_2 = frequency_2.sort_values(by=['index'], ascending=False)
    frequency_2['probability'] = (frequency_2["index"] / qty_games)
    os.remove('tmp_data_2.csv')
    with open("tmp_data_2.csv", "w") as file:
        frequency_2.to_csv(file)
    return frequency_2

def triple_balls_combination(result_df, qty_games): 
    if os.path.isfile('tmp_data_3.csv'):
        os.remove('tmp_data_3.csv')
        
    with open("tmp_data_3.csv", "a") as file:        
        for i in range(1, 6):
            bola1 = 'Bola' + str(i)
            for j in range(i+1, 7):
                bola2 = 'Bola' + str(j)
                for k in range(j+1,7):
                    bola3 = 'Bola' + str(k)
                    if (i!=j and j!=k and i!=k):
                        result1 = pd.DataFrame(result_df.groupby([bola1, bola2, bola3])['index'].nunique())
                        result1.to_csv(file)
                    
    final_result = pd.read_csv("tmp_data_3.csv")
    df_remove = final_result.loc[(final_result['index'] == 'index')]
    final_df = final_result.drop(df_remove.index, axis=0).reset_index(drop=True)
    final_df = final_df.rename_axis('index1').reset_index()
    final_df['index'] = pd.to_numeric(final_df['index'])
    frequency_3 = pd.DataFrame(final_df.groupby(['Bola1', 'Bola2', 'Bola3'])['index'].sum())
    frequency_3 = frequency_3.sort_values(by=['index'], ascending=False)
    frequency_3['probability'] = (frequency_3["index"] / qty_games)
    os.remove('tmp_data_3.csv')
    with open("tmp_data_3.csv", "w") as file:
        frequency_3.to_csv(file)
    return frequency_3
    
def quadri_balls_combination(result_df, qty_games): 
    if os.path.isfile('tmp_data_4.csv'):
        os.remove('tmp_data_4.csv')
        
    with open("tmp_data_4.csv", "a") as file:        
        for i in range(1, 6):
            bola1 = 'Bola' + str(i)
            for j in range(i+1, 7):
                bola2 = 'Bola' + str(j)
                for k in range(j+1,7):
                    bola3 = 'Bola' + str(k)
                    for l in range(k+1,7):
                        bola4 = 'Bola' + str(l)
                        if (i!=j and j!=k and k!=l):
                            result1 = pd.DataFrame(result_df.groupby([bola1, bola2, bola3, bola4])['index'].nunique())
                            result1.to_csv(file)
                    
    final_result = pd.read_csv("tmp_data_4.csv")
    df_remove = final_result.loc[(final_result['index'] == 'index')]
    final_df = final_result.drop(df_remove.index, axis=0).reset_index(drop=True)
    final_df = final_df.rename_axis('index1').reset_index()
    final_df['index'] = pd.to_numeric(final_df['index'])
    frequency_4 = pd.DataFrame(final_df.groupby(['Bola1', 'Bola2', 'Bola3', 'Bola4'])['index'].sum())
    frequency_4 = frequency_4.sort_values(by=['index'], ascending=False)
    frequency_4['probability'] = (frequency_4["index"] / qty_games)
    os.remove('tmp_data_4.csv')
    with open("tmp_data_4.csv", "w") as file:
        frequency_4.to_csv(file)
    return frequency_4

def games_never_shown(result_df):
    key_list = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']
    new_result_df = result_df[['index', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Soma']].copy(deep=True)
    
    #Analisando todas as probabilidades do jogo
    comb = list(combinations(range(1,61),6))
    print('The total probability is:',len(comb))
    all_comb_df = pd.DataFrame(comb, columns = key_list)
    all_comb_df['Soma'] = all_comb_df.sum(axis=1)
    
    #Excluir colunas com soma menor e maior que um número estipulado
    indexNames = all_comb_df.loc[(all_comb_df['Soma'] < 143) | (all_comb_df['Soma'] > 223)]
    new_all_comb_df = pd.DataFrame(all_comb_df.drop(indexNames.index, axis=0).reset_index())
    print('The total probability after take off settled range number is:',len(new_all_comb_df))
    
    # Comparando com jogos passados e excluindo os que já saíram
    index_to_remove = pd.DataFrame(new_all_comb_df.isin(new_result_df))
    index_to_remove.drop(['index', 'Soma'], axis = 1, inplace = True)
    index_to_remove['Result'] = ( index_to_remove['Bola1'] & index_to_remove['Bola2'] & index_to_remove['Bola3'] & index_to_remove['Bola4'] & index_to_remove['Bola5'] & index_to_remove['Bola6'] )
    indexNames1 = index_to_remove.loc[(index_to_remove['Result'] == True)]
    new_all_comb_df = new_all_comb_df.drop(indexNames1.index, axis=0).reset_index()
    print('The total probability after take off all shown number is:',len(new_all_comb_df))  
    os.remove('total_probabilities.csv')
    with open("total_probabilities.csv", "w") as file:
        new_all_comb_df.to_csv(file)  
    return new_all_comb_df

def write_file(load_dataframe):
    if os.path.isfile('resultado.csv'):
        os.remove('resultado.csv')
    load_dataframe.to_csv("resultado.csv")
    return True

#Start of project with time stamps
starttime = time.time()
print('Analysis Started at:', starttime)
result_df = load_file()
qty_games = result_df['Concurso'].count()
print(result_df.describe())
print(result_df['Soma'].mean())

startgamesnevershown = time.time()
games_never_shown_df = games_never_shown(result_df)
endgamesnevershown = time.time()
print('The procedure games_never_shown took ', endgamesnevershown-startgamesnevershown)

startballsfrequency = time.time()
balls_frequency_df = frequencies_of_ball(result_df, qty_games)
endballsfrequency = time.time()
print('The procedure balls_frequency took ', endballsfrequency-startballsfrequency)

startdoubleballsfrequency = time.time()
double_balls_comb_df = double_balls_combination(result_df, qty_games)
enddoubleballsfrequency = time.time()
print('The procedure double_balls_frequency took ', enddoubleballsfrequency-startdoubleballsfrequency)

starttripleballsfrequency = time.time()
triple_balls_comb_df = triple_balls_combination(result_df, qty_games)
endtripleballsfrequency = time.time()
print('The procedure triple_balls_frequency took ', endtripleballsfrequency-starttripleballsfrequency)

startquadriballsfrequency = time.time()
quadri_balls_comb_df = quadri_balls_combination(result_df, qty_games)
endquadriballsfrequency = time.time()
print('The procedure quadri_balls_frequency took ', endquadriballsfrequency-startquadriballsfrequency)

endtime = time.time()
print("DONE!! PLEASE CHECK OUT THE FILE resultado.csv... Time to process:", endtime-starttime)
