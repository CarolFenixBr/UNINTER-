#importando bibliotecas necessárias:
import pandas as pd
from google.colab import drive, files
from matplotlib import pyplot as plt

#montagem do google drive
drive.mount('/content/drive')

#importando arquivo stores.csv
df = pd.read_csv('/content/drive/MyDrive/UNINTER/2023/LINGUAGEM DE PROGRAMAÇÃO/Trabalho pratico/Stores.csv', sep=',', encoding='ISO 8859-1')
df.head()

df.columns.values

dfColunas = ['ï»¿Store ID ', 'Store_Area', 'Items_Available','Daily_Customer_Count', 'Store_Sales']

dfFiltrado = df.filter(items=dfColunas)
dfFiltrado = dfFiltrado.rename(columns={
    'ï»¿Store ID ':'ID',
    'Store_Area':'Itens',
    'Items_Available':'Disponibilidade',
    'Daily_Customer_Count':'Visitantes',
    'Store_Sales':'Vendas(Dolar)'
})
dfFiltrado

#Testes estáticos:
print('\nItens:')
dados = dfFiltrado['Itens']
print(dados.values.max())  # retorna o valor máximo
print(dados.values.min())  # retorna o valor mínimo
print(dados.values.mean()) # retorna a média
print(dados.values.std())  # retorna o desvio padrão

#Gráfico com o título
plt.title('Itens')

plt.grid()

#plotando os resultados obtidos por x e y
plt.plot(dados.values.max(), marker="o", markersize=15, markerfacecolor='red')
plt.plot(dados.values.min(), marker="o",markersize=15, markerfacecolor='blue')
plt.plot(dados.values.mean(), marker="o",markersize=15, markerfacecolor='green')
plt.plot(dados.values.std(),marker="o",markersize=15, markerfacecolor='black')
plt.show

print('\nDisponibilidade:')
dados = dfFiltrado['Disponibilidade']
print(dados.values.max())  # retorna o valor máximo
print(dados.values.min())  # retorna o valor mínimo
print(dados.values.mean()) # retorna a média
print(dados.values.std())  # retorna o desvio padrão

print('\nVisitantes')
dados = df['Daily_Customer_Count']
print(dados.values.max())
print(dados.values.min())
print(dados.values.mean())
print(dados.values.std())

plt.title('Visitantes')

plt.grid()

#plotando os resultados obtidos por x e y
plt.plot(dados.values.max(), marker="o", markersize=15, markerfacecolor='red')
plt.plot(dados.values.min(), marker="o",markersize=15, markerfacecolor='blue')
plt.plot(dados.values.mean(), marker="o",markersize=15, markerfacecolor='green')
plt.plot(dados.values.std(),marker="o",markersize=15, markerfacecolor='black')
plt.show

print('\nVendas em dolar')
dados = dfFiltrado['Vendas(Dolar)']
print(dados.values.max())  # retorna o valor máximo
print(dados.values.min())  # retorna o valor mínimo
print(dados.values.mean()) # retorna a média
print(dados.values.std())  # retorna o desvio padrão

plt.title('Vendas em dolar')

plt.grid()

#plotando os resultados obtidos por x e y
plt.plot(dados.values.max(), marker="o", markersize=15, markerfacecolor='red')
plt.plot(dados.values.min(), marker="o",markersize=15, markerfacecolor='blue')
plt.plot(dados.values.mean(), marker="o",markersize=15, markerfacecolor='green')
plt.plot(dados.values.std(),marker="o",markersize=15, markerfacecolor='black')
plt.show
