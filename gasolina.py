import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
with sns.axes_style('whitegrid'): 

    grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
    grafico.figure.set_size_inches(w=25/2.54, h=25/2.54)
    grafico.set_title('Preco da gasolina por dia', fontsize=20, fontweight='bold')
    grafico.set_xlabel('Dia do mês', fontsize=15, fontweight='bold')
    grafico.set_ylabel('Preço em R$', fontsize=15, fontweight='bold')