import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt

dataset = pd.read_csv('dados/Churn.csv', sep = ';')

print(dataset.head())
print(dataset.shape)

dataset.columns = ['id', 'score', 'estado', 'genero', 'idade', 'patrimonio', 'saldo', 'produtos', 'temcartaocredito', 'ativo', 'salario', 'saiu']

print(dataset.head())

# Explorar dados categoricos
# agrupado = dataset.groupby(['estado']).size()
# print(agrupado)
# agrupado.plot.bar(color = 'gray')
# plt.show()

# agrupado = dataset.groupby(['genero']).size()
# print(agrupado)
# agrupado.plot.bar(color = 'gray')
# plt.show()

# Explorar colunas numéricas
# print(dataset['score'].describe())
# srn.boxplot(dataset['score']).set_title('Score')
# plt.show()
# srn.displot(dataset['score']).set_titles('Score')
# plt.show()

# print(dataset['idade'].describe())
# srn.boxplot(dataset['idade']).set_title('Idade')
# plt.show()
# srn.displot(dataset['idade']).set_titles('Idade')
# plt.show()

# print(dataset['saldo'].describe())
# srn.boxplot(dataset['saldo']).set_title('Saldo')
# plt.show()
# srn.displot(dataset['saldo']).set_titles('Saldo')
# plt.show()

# print(dataset['salario'].describe())
# srn.boxplot(dataset['salario']).set_title('Salário')
# plt.show()
# srn.displot(dataset['salario']).set_titles('Salário')
# plt.show()

# print(dataset.isnull().sum())