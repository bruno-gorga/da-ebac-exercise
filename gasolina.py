import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
with sns.axes_style('whitegrid'): 

    grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='dark')
    grafico.set(title='Preco da gasolina por dia', xlabel='Dia', ylabel='Preço em R$')

grafico.figure.savefig(fname='gasolina.png')