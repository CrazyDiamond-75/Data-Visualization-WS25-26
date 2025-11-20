import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
import math
import random

# number of plots
n = 2

cols = round(n ** 0.5)
rows = math.ceil(n / cols)
fig, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows), sharex=True, sharey=True)

# hardcode limits because random data may make scales wonky otherwise
plt.ylim(-0.1, 1.1)
plt.yticks([]) # disable axis labels, since it's random data anyways
plt.xticks([])


axes = axes.flatten()
aspect = .5 # aspect ratio of the graphs (there's probably a better way to get pyplot to make non-square graphs but this works i guess)
fig.set_figwidth(8)

colors = list(TABLEAU_COLORS.keys())


# Window size for moving average to make randomness seem more natural
wdw = 4

pointcount = 20

ys1 = np.convolve(np.random.default_rng().random(pointcount), np.ones(wdw) / wdw, mode="valid")
ys2 = np.convolve(np.random.default_rng().random(pointcount), np.ones(wdw) / wdw, mode="valid")
xs = np.arange(ys1.shape[0])

# scatter-ish plot
axes[0].scatter(xs, ys1, marker='o', color=colors[0 % len(colors)])
axes[0].scatter(xs, ys2, marker='s', color=colors[0 % len(colors)])
axes[0].set_title("")

# line plot
axes[1].plot(xs, ys1, marker='o', color=colors[1 % len(colors)])
axes[1].plot(xs, ys2, marker='s', color=colors[1 % len(colors)])
axes[1].set_title("")

# "circling" of maximum
idx_max = np.argmax(ys1)
csize = 3
circle = patches.Ellipse((xs[idx_max], ys1[idx_max]), 1 * 3, .3 * 3, fill=False, linestyle="--")
#axes[1].set_aspect("equal", adjustable="datalim")
axes[1].add_patch(circle)



plt.tight_layout()
plt.savefig("2.3.pdf")
plt.show()