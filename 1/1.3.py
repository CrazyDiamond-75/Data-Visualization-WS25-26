import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Store the dataset in a df, while specifying the header, separator, and decimal period.
df = pd.read_csv('kochin.CSV', header=0, sep=';', decimal=',')
# Set the index to the year for easier plotting later.
df = df.set_index('YEAR')
# Normalize all attribute values by subtracting their mean and dividing their standard deviation.
df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns, index=df.index)

#### PLOT FOR 1.3.4 and 1.3.5 ####
# Columns we want for the first plot.
cols = ['UNEMP', 'BWRATIO,', 'NNP'] # df.columns

# Generate one plot only, specify the figure size.
fig, ax = plt.subplots(figsize=(16,9))
years = list(df.index.values)

for cname in cols:
    col = df[cname]
    ax.plot(col, label=cname)

ax.set_xlabel('Years')
ax.set_xticks(years)
ax.set_ylabel('Normalized scale')
ax.set_yticks([])
ax.set(xlim=(years[0], years[-1]))
ax.set_title('Unemployment did not strongly correlate with net national product or benefit/wage ratio')
ax.legend()

#plt.savefig('1.3.45.pdf')

#### PLOT FOR 1.3.7 ####
# Columns we want for the first plot.
cols = ['UNEMP', 'DEMAND'] # df.columns

# Generate one plot only, specify the figure size.
fig, ax = plt.subplots(figsize=(16,9))
years = list(df.index.values)

for cname in cols:
    col = df[cname]
    ax.plot(col, label=cname)

ax.set_xlabel('Years')
ax.set_xticks(years)
ax.set_ylabel('Normalized scale')
ax.set_yticks([])
ax.set(xlim=(years[0], years[-1]))
ax.set_title('Unemployment correlated with demand')
ax.legend()

plt.savefig('1.3.7.pdf')

