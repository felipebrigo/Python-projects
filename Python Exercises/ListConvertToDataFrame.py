import pandas as pd
import numpy as np

lista=['1986/1986', '40000 km', 'São Paulo - SP', '2000/2000', '100 km', 'Santo André - SP', '1990/1990', '195558 km', 'Indaiatuba - SP', '1993/1993', '197441 km', 'Araraquara - SP', '1996/1996', '160000 km', 'São Paulo - SP', '1997/1997', '90000 km', 'Carapicuíba - SP', '1993/1993', '100 km', 'Araraquara - SP', '1982/1983', '42597 km', 'Embu das Artes - SP', '1991/1991', '150000 km', 'Botucatu - SP', '1990/1990', '191000 km', 'São Paulo - SP', '2002/2002', '100000 km', 'São Paulo - SP', '1995/1995', '285000 km', 'São Bernardo do Campo - SP', '1992/1992', '230000 km', 'São José do Rio Preto - SP', '1994/1995', '100 km', 'Araraquara - SP', '1997/1997', '181000 km', 'São Paulo - SP', '1997/1998', '170000 km', 'São Paulo - SP', '1997/1997', '61555 km', 'São Paulo - SP', '1994/1994', '155600 km', 'São José do Rio Preto - SP', '1997/1997', '117000 km', 'São Paulo - SP', '1991/1991', '100 km', 'São Bernardo do Campo - SP', '1995/1995', '103870 km', 'Santos - SP', '2000/2000', '115006 km', 'São Paulo - SP', '1995/1995', '83500 km', 'Guaíra - SP', '1989/1989', '20000 km', 'São Paulo - SP']

dados = pd.DataFrame(np.array(lista).reshape(-1,3))
print(dados)