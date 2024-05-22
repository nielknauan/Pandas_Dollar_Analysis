import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
caminho_arquivo = r''
df = pd.read_excel(caminho_arquivo)

# Converter a coluna de data para o tipo datetime, se necessário
df['Data Cotacao'] = pd.to_datetime(df['Data Cotacao'])

# Extrair o ano da coluna de data e criar uma nova coluna chamada 'Ano'
df['Ano'] = df['Data Cotacao'].dt.year

# Calcular estatísticas resumidas sobre os valores do dólar ao longo dos anos
analise_dolar_por_ano = df.groupby('Ano')['Dolar'].describe()

# Exibir o gráfico
ax = analise_dolar_por_ano['mean'].plot(kind='line', marker='o', linestyle='-', color='b', figsize=(10, 6))
plt.title('Média do valor do dólar por ano')
plt.xlabel('Ano')
plt.ylabel('Valor médio do dólar')
plt.grid(True)

# Adicionar os valores em cima dos pontos
for x, y in zip(analise_dolar_por_ano.index, analise_dolar_por_ano['mean']):
    ax.text(x, y, f'{y:.2f}', ha='center', va='bottom')

plt.show()
