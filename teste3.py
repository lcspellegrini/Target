import pandas as pd
import json


with open('dados (1).json') as file:
    dados = json.load(file)

df = pd.DataFrame(dados)
dias_uteis = df[df['valor'] > 0]
menor_valor = dias_uteis['valor'].min()
maior_valor = dias_uteis['valor'].max()
media_mensal = dias_uteis['valor'].mean()
dias_melhores = df[df['valor'] > media_mensal].shape[0]

print(menor_valor)
print(maior_valor)
print(media_mensal)
print(dias_melhores)