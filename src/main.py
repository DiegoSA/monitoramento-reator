""" Programing Exercise"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def interpretar(colunas, fator_correlacao):
    print(f"A Correlação entre as colunas: {colunas[0]} e {colunas[1]} tem um coefidiente de: {fator_correlacao:3f} e")
    valor = abs(fator_correlacao)

    if valor < 0.20:
        return f"é interpretada como muito fraca.\n"

    elif valor < 0.40:
        return f"é interpretada como fraca.\n"

    elif valor < 0.60:
        return f"é interpretada como moderada.\n"

    elif valor < 0.80:
        return f"é interpretada como forte.\n"

    else:
        return f"é interpretada como muito forte.\n"

df = pd.read_csv("/workspaces/monitoramento-reator/data/process.csv")

df['reactor_temp'].hist()
plt.savefig("/workspaces/monitoramento-reator/images/reactor_temp.png")

plt.close()


cp = df['ambient_temp_effect']
mu = cp.mean()
sigma = cp.std()
vlr_min = cp.min()
vlr_max = cp.max()
print(f"a média da coluna ambient_temp_effect é: {round(mu,2)}, \no desvio padrão é: {round(sigma,2)}, \no valor mínimo: {round(vlr_min,2)} \ne o valor máximo: {round(vlr_max,2)}.")


A = []
B = []

for i in range(len(df)):
  match df.at[i, 'operating_regime']:
    case 'A':
      A.append(df.at[i, 'reactor_temp'])
    case 'B':
      B.append(df.at[i, 'reactor_temp'])

med_temp_normal = np.nanmean(A)
med_temp_estresse = np.nanmean(B)

print(f"média temperatura em estresse é: {round(med_temp_estresse, 2)} \nmédia temperatura normal é: {round(med_temp_normal, 2)}")


A_mean = df[df['operating_regime'] == 'A']['reactor_temp'].mean()
B_mean = df[df['operating_regime'] == 'B']['reactor_temp'].mean()

print ('A média da temperatura do reator em funcionamento Normal é: ', round(A_mean, 2))
print ('A média da temperatura do reator em funcionamento sob estresse é: ', round(B_mean, 2))

print("\nCORRELAÇÕES DE PEARSON\n")

relacao_a = ['reactor_temp', 'reactor_pressure']
correlacao_a = df[relacao_a[0]].corr(df[relacao_a[1]], method='pearson')
print(interpretar(relacao_a, correlacao_a))

relacao_b = ['feed_flow_rate', 'power_consumption_kw']
correlacao_b = df[relacao_b[0]].corr(df[relacao_b[1]], method='pearson')
print(interpretar(relacao_b, correlacao_b))

relacao_c = ['selectivity', 'yield_pct']
correlacao_c = df[relacao_c[0]].corr(df[relacao_c[1]], method='pearson')
print(interpretar(relacao_c, correlacao_c))

relacao_d = ['ambient_temp_effect', 'reaction_rate']
correlacao_d = df[relacao_d[0]].corr(df[relacao_d[1]], method='pearson')
print(interpretar(relacao_d, correlacao_d))




