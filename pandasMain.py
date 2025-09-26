import pandas as pd

# Criando dicionários com nomes e idades
dados = {
    'Nome': ['Victoria', 'Marcelo', 'Alex', 'Pedro', 'Monica'],
    'Idade': [19, 20, 20, 21, 25]  # Removidas as aspas para serem inteiros
}

# Criando uma série a partir do dicionário criado
serieIdades = pd.Series(dados['Idade'], index=dados['Nome'])

# Imprimindo a série de idades
print("Série de Idades:")
print(serieIdades)
print()  # Linha em branco para separar

# Agora calculando a média de idades
mediaIdades = serieIdades.mean()
print("Média de idades:", mediaIdades)