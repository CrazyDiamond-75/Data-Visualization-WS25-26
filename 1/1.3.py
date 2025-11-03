import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
from sklearn.preprocessing import StandardScaler,MinMaxScaler #scikit-learn package

# Store the dataset in a df, while specifying the header, separator, and decimal period.
df = pd.read_csv('kochin.CSV', header=0, sep=';', decimal=',')
df = df.set_index('YEAR')
df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns, index=df.index)

cols = ['UNEMP', 'BWRATIO,', 'NNP'] # df.columns

fig, ax = plt.subplots(figsize=(16,9))
years = list(df.index.values)

for cname in cols:
    col = df[cname]
    ax.plot(col, label=cname)

ax.set_xlabel('Years')
ax.set_xticks(years)
ax.set_ylabel('Normalized attributes')
ax.set_yticks([])
ax.set(xlim=(years[0], years[-1]))
ax.set_title('Unemployment does not strongly correlate with net national product or benefit/wage ratio')
ax.legend()

plt.savefig('1.3.4.pdf')

