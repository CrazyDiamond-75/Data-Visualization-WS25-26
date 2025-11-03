import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
import math

# Store the dataset in a df, while specifying the header from the tsv
df = pd.read_csv('DatasaurusDozen.tsv', sep='\t', header=0)
# We have exactly so many datasets in the df as there are unique values of the "dataset" attribute.
n = len(df['dataset'].unique())

# We find the integer product cols * rows >= n, such that cols and rows are minimal.
# This is done to find the number of subplots in our graph, such that it appears as "square" as can be.
cols = round(n ** 0.5)
rows = math.ceil(n / cols)

# Generate subplots for each row and column.
fig, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows), sharex=True, sharey=True)
axes = axes.flatten()

# We iterate through i < n, to assign each plot a colour.
i = 0
colors = list(TABLEAU_COLORS.keys())
# For each subplot, we assign one name, dataset pair.
for ax, (name, ds) in zip(axes, df.groupby('dataset')):
    # Calculate the mean and variance x and y on the fly using numpy.
    print(f"M=({np.mean(ds['x']):.4f}, {np.mean(ds['y']):.4f})\tV=({np.var(ds['x']):.4f}, {np.var(ds['y']):.4f})")
    # Plot each ds as a scatterplot as needed.
    ax.scatter(ds['x'], ds['y'], marker='.', color=colors[i % len(colors)])
    ax.set_title(name)
    i += 1

# Hide empty plots, as cols * rows <= n.
for ax in axes[n:]:
    ax.set_visible(False)

plt.tight_layout()
plt.savefig("1.2.pdf")
