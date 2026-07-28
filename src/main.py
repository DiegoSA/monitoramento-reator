""" Programing Exercise"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/workspaces/monitoramento-reator/data/process.csv")

df['reactor_temp'].hist()
plt.savefig("/workspaces/monitoramento-reator/images/reactor_temp.png")

plt.close()