# Importando Bibliotecas e Carregando o Dataset
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset 'tips'
tips = sns.load_dataset('tips')

# Número de Registros, Tipos de Dados e Descrição das Features
# Número de registros e tipos de dados
print(tips.info())
# Descrição das features
print(tips.describe(include='all'))

# Resumos Estatísticos Numéricos, Contagem de Valores e Distribuição dos Dados
# Resumo estatístico numérico
print(tips.describe())

# Contagem de valores para variáveis categóricas
print(tips['sex'].value_counts())
print(tips['smoker'].value_counts())
print(tips['day'].value_counts())
print(tips['time'].value_counts())

# Elaboração de Hipóteses e Confirmação/Refutação
'''
    Hipótese 1: O total da conta (total_bill) tem uma correlação positiva com a gorjeta (tip).
    Hipótese 2: A média de gorjetas dadas por homens é maior que a média de gorjetas dadas por mulheres.
    Hipótese 3: Clientes que fumam (smoker) dão gorjetas maiores que clientes que não fumam.
    Hipótese 4: As gorjetas são maiores aos fins de semana (sábado e domingo) do que nos dias de semana.
    Hipótese 5: O período do jantar (dinner) tem gorjetas maiores do que o período do almoço (lunch).
    Hipótese 6: Grupos maiores de clientes resultam em gorjetas maiores.

Vamos analisar cada uma dessas hipóteses com visualizações e cálculos estatísticos.
'''

# Gráficos e Análise das Hipóteses
# Hipótese 1: Correlação entre total_bill e tip
# Gráfico de dispersão
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Total Bill vs Tip')
plt.show()

# Cálculo da correlação
correlation = tips['total_bill'].corr(tips['tip'])
print(f"Correlação entre total_bill e tip: {correlation}")

# Hipótese 2: Média de gorjetas por sexo
# Gráfico de barras
sns.barplot(data=tips, x='sex', y='tip', estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Sexo')
plt.show()

# Teste t para diferença de médias
from scipy.stats import ttest_ind

male_tips = tips[tips['sex'] == 'Male']['tip']
female_tips = tips[tips['sex'] == 'Female']['tip']
t_stat, p_val = ttest_ind(male_tips, female_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Hipótese 3: Gorjetas por clientes que fumam vs. não fumam
# Gráfico de barras
sns.barplot(data=tips, x='smoker', y='tip', estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Clientes Fumantes vs Não Fumantes')
plt.show()

# Teste t para diferença de médias
smoker_tips = tips[tips['smoker'] == 'Yes']['tip']
non_smoker_tips = tips[tips['smoker'] == 'No']['tip']
t_stat, p_val = ttest_ind(smoker_tips, non_smoker_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Hipótese 4: Gorjetas por dia da semana
# Gráfico de barras
sns.barplot(data=tips, x='day', y='tip', estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Dia da Semana')
plt.show()

# Comparação específica para fins de semana vs dias de semana
weekend_tips = tips[tips['day'].isin(['Sat', 'Sun'])]['tip']
weekday_tips = tips[~tips['day'].isin(['Sat', 'Sun'])]['tip']
t_stat, p_val = ttest_ind(weekend_tips, weekday_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Hipótese 5: Gorjetas por período do dia
# Gráfico de barras
sns.barplot(data=tips, x='time', y='tip', estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Período do Dia')
plt.show()

# Teste t para diferença de médias
dinner_tips = tips[tips['time'] == 'Dinner']['tip']
lunch_tips = tips[tips['time'] == 'Lunch']['tip']
t_stat, p_val = ttest_ind(dinner_tips, lunch_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Hipótese 6: Gorjetas por tamanho do grupo
# Gráfico de dispersão com linha de tendência
sns.scatterplot(data=tips, x='size', y='tip')
sns.lineplot(data=tips, x='size', y='tip', errorbar=None)
plt.title('Gorjetas por Tamanho do Grupo')
plt.show()

# Análise estatística
grouped_tips = tips.groupby('size')['tip'].mean()
print(grouped_tips)

# Gráficos de Distribuição
# Boxplot para total_bill por day
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Distribuição de Total Bill por Dia')
plt.show()

# Histograma para tip
sns.histplot(tips['tip'], bins=20, kde=True)
plt.title('Distribuição das Gorjetas')
plt.show()
