import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
import math

# Store the dataset in a df, while specifying the header from the csv
df = pd.read_csv('kochin.CSV', header=0)

fig, axes = plt.subplots()
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
