from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
import os

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
    #print(result_df)
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
    #print(result_df)
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
    #print(result_df)
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

def write_file(load_dataframe):
    load_dataframe.to_csv("resultado.csv")
    return True

result_df = load_file()
qty_games = result_df['Concurso'].count()
print(result_df.describe())
print(result_df['Soma'].mean())
balls_frequency_df = frequencies_of_ball(result_df, qty_games)
double_balls_comb_df = double_balls_combination(result_df, qty_games)
triple_balls_comb_df = triple_balls_combination(result_df, qty_games)
quadri_balls_comb_df = quadri_balls_combination(result_df, qty_games)