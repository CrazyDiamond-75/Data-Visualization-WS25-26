import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
import math


def nearest_sqrt(n: int):
    sqrt = n**0.5
    sqrtC = math.ceil(sqrt)
    sqrtF = math.floor(sqrt)

    if abs(sqrt - sqrtC) <= abs(sqrt - sqrtF):
        return sqrtC
    else:
        return sqrtF


df = pd.read_csv('DatasaurusDozen.tsv', sep='\t', header=0)
n = len(df['dataset'].unique())
cols = nearest_sqrt(n)
rows = math.ceil(n / cols)

fig, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows), sharex=True, sharey=True)
axes = axes.flatten()

i = 0
colors = list(TABLEAU_COLORS.keys())
for ax, (name, ds) in zip(axes, df.groupby('dataset')):
    print(f"M=({np.mean(ds['x']):.4f}, {np.mean(ds['y']):.4f})\tV=({np.var(ds['x']):.4f}, {np.var(ds['y']):.4f})")
    ax.scatter(ds['x'], ds['y'], marker='.', color=colors[i % len(colors)])
    ax.set_title(name)
    i += 1

# Hide empty plots
for ax in axes[n:]:
    ax.set_visible(False)

plt.tight_layout()
plt.savefig("1.2.pdf")
