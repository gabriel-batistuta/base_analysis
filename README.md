# Sobre
esta é uma analise da base de dados **"tips"** do seaborn feita para a disciplina de Tópicos Especiais em Engenharia de Software

# Referências:
- https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
- https://www.kaggle.com/datasets/ranjeetjain3/seaborn-tips-dataset
- https://seaborn.pydata.org/tutorial/introduction.html

## Correlação entre Total da Conta e Gorjeta
```python
# Gráficos e Análise das Hipóteses
# Hipótese 1: Correlação entre Total da Conta e Gorjeta
# Gráfico de dispersão
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Conta total vs Gorjeta')
plt.show()

# Cálculo da correlação
correlation = tips['total_bill'].corr(tips['tip'])
print(f"Correlação entre total_conta e gorjeta: {correlation}")

# conclusão:
# quanto maior o número da conta maior o valor dado da gorjeta
# e menor o número de gorjetas dadas pelo cliente

# então pode-se dizer que se o preço for razoavelmente baixo
# o cliente irá pagar a gorjeta
```
![conta vs gorjeta](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/ef970e5b-2a2c-4e0a-869b-28d8f16eb7d7)

## Média de gorjetas por sexo
```python
# Hipótese 2: Média de gorjetas por sexo
# Gráfico de barras
sns.barplot(data=tips, x='sex', y='tip',
            estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Sexo')
plt.show()

# Teste t para diferença de médias
male_tips = tips[tips['sex'] == 'Male']['tip']
female_tips = tips[tips['sex'] == 'Female']['tip']
t_stat, p_val = ttest_ind(male_tips, female_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# conclusão:
# a diferença de gorjetas por sexo é minima
# então podemos dizer que:
# a gorjeta dada é independente do sexo do cliente
```
![medias de gorjeta por sexo](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/e401bec2-f188-4910-9780-f83dff39afbe)

## Gorjetas por clientes que fumam vs. não fumam
```python
# Hipótese 3: Gorjetas por clientes que fumam vs. não fumam
# Gráfico de barras
sns.barplot(data=tips, x='smoker', y='tip',
            estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Clientes Fumantes vs Não Fumantes')
plt.show()

# Teste t para diferença de médias
smoker_tips = tips[tips['smoker'] == 'Yes']['tip']
non_smoker_tips = tips[tips['smoker'] == 'No']['tip']
t_stat, p_val = ttest_ind(smoker_tips, non_smoker_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Conclusão
# assim como a questão do sexo, a diferença é quase nula
# portanto a gorjeta também é independente de fumar ou não
```
![média de clientes fumantes e não fumantes](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/e96c4be7-9cfb-4e0e-b4e3-fac652481a21)

## Gorjetas por dia da semana
```python
# Hipótese 4: Gorjetas por dia da semana
# Gráfico de barras
sns.barplot(data=tips, x='day', y='tip',
            estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Dia da Semana')
plt.show()

# Comparação específica para fins de semana vs dias de semana
weekend_tips = tips[tips['day'].isin(['Sat', 'Sun'])]['tip']
weekday_tips = tips[~tips['day'].isin(['Sat', 'Sun'])]['tip']
t_stat, p_val = ttest_ind(weekend_tips, weekday_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Conclusão:
# Sábado e Domingo a gorjeta é levemente maior que na semana
# é possível que:
# os clientes estejam com mais dinheiro no final de semana
# se sentem mais a vontade em gastar no final de semana
```
![media de gorjetas por dia da semana](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/4af9c15a-a128-4b6c-95b2-1b44c05d40a9)

## Gorjetas por período do dia
```python
# Hipótese 5: Gorjetas por período do dia
# Gráfico de barras
sns.barplot(data=tips, x='time', y='tip',
            estimator=lambda x: sum(x)/len(x))
plt.title('Média de Gorjetas por Período do Dia')
plt.show()

# Teste t para diferença de médias
dinner_tips = tips[tips['time'] == 'Dinner']['tip']
lunch_tips = tips[tips['time'] == 'Lunch']['tip']
t_stat, p_val = ttest_ind(dinner_tips, lunch_tips)
print(f"T-Stat: {t_stat}, P-Value: {p_val}")

# Conclusão:
# os clientes dão mais gorjetas em quantidade durante:
# jantar > almoço (por uma diferença bem baixa)
# portanto, os clientes preferem pagar pelas gorjetas no fim do dia
```
![gorjetas por periodo do dia](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/9a02873b-ba6e-468b-89a1-be5d999408e1)

## Gorjetas por tamanho do grupo
```python
# Hipótese 6: Gorjetas por tamanho do grupo
# Gráfico de dispersão com linha de tendência
sns.scatterplot(data=tips, x='size', y='tip')
sns.lineplot(data=tips, x='size',
             y='tip', errorbar=None)
plt.title('Gorjetas por Tamanho do Grupo')
plt.show()

# Análise estatística
grouped_tips = tips.groupby('size')['tip'].mean()
print(grouped_tips)

# Conclusão:
# A média de gorjetas é maior com um grupo de 2 a 4 pessoas
# e um valor semelhante em todos os outros tamanhos (1, 5, 6)
# Supostamente, os clientes preferem:
# pagar mais gorjetas com um grupo pequeno de pessoas
# em relação ao preço:
# preferem pagar o valor de acordo com o do pedido, crescentemente.
```
![Gorjetas por tamanho de grupo](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/1bb002de-ecb0-4d4c-934f-cf6b820d5190)

## Gráficos de Distribuição
```python
# Histograma para gorjeta
sns.histplot(tips['time'])
plt.title('Distribuição das Gorjetas')
plt.show()
```
![distribuição de gorjetas](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/563b9740-7eaf-47be-9ba7-1d45bb97ff37)

```python
# Histograma para Fumantes
sns.histplot(tips['smoker'])
plt.title('Distribuição de Fumantes')
plt.show()
```
![distribuição de fumantes](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/83bb6076-09de-41f7-a722-eb20467d3343)

## Gráficos temporais
```python
# Adicionando Gráficos de Velas e de Séries Temporais
# Criando uma série temporal sintética de gorjetas
# valores ficticeos para a linha de tempo
np.random.seed(0)
dates = pd.date_range(start='2021-01-01',
                      periods=len(tips), freq='D')
tips['date'] = dates
tips = tips.sort_values('date')
```
```python
# Gráfico de Série Temporal para Gorjetas
plt.figure(figsize=(10, 6))
plt.plot(tips['date'], tips['tip'], label='Tip')
plt.title('Série Temporal de Gorjetas')
plt.xlabel('Data')
plt.ylabel('Gorjeta')
plt.legend()
plt.show()
```
![serie temporal de gorjetas](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/a03a808d-2757-41bb-bdfd-f2290baf9c95)

```python
# Gráfico de Velas para Gorjetas
# Preparar dados para o gráfico de velas
tips['open'] = tips['tip'].shift(1)
tips['high'] = tips[['tip', 'open']].max(axis=1)
tips['low'] = tips[['tip', 'open']].min(axis=1)
tips['close'] = tips['tip']
# Remover NaN resultante do shift
tips = tips.dropna()
# Dados para o gráfico de velas
candle_data = tips[['date', 'open', 'high', 'low', 'close']].set_index('date')
# Plotando gráfico de velas
mpf.plot(candle_data, type='candle', style='charles',
         title='Gráfico de Velas de Gorjetas', ylabel='Gorjeta')
```
![grafico de velas de gorjetas](https://github.com/gabriel-batistuta/base_analysis/assets/96501194/03821a40-b1dd-4ea8-9445-7985372a5407)





