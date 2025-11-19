import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
import numpy as np #nunpy haha
import math
import random


# number of plots
n = 4

cols = round(n ** 0.5)
rows = math.ceil(n / cols)
fig, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows), sharex=True, sharey=True)

# hardcode limits because random data may make scales wonky otherwise
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

axes = axes.flatten()
colors = list(TABLEAU_COLORS.keys())

####################
# a)
####################

# Fig 1
pcount = 20
xs = [math.sin(x*math.pi*2.0/pcount) for x in range(pcount)]
ys = [math.cos(x*math.pi*2.0/pcount) for x in range(pcount)]
axes[0].scatter(xs, ys, marker='.', color=colors[0 % len(colors)])
axes[0].set_title("a) 1")


# Fig 2
# - Law of proximity
# - Law of connection
# - Percieved as a filled right triangle

# Fig 3
pcount = 10 # per line
xs = [-1] * (pcount+1) + [1] * (pcount+1) + [x / pcount * 2 - 1 for x in range(pcount)] # wtf am i doing here
ys = [x / pcount * 2 - 1 for x in range(pcount+1)] * 2 + [-1] * pcount
axes[1].scatter(xs, ys, marker='.', color=colors[1 % len(colors)])
axes[1].set_title("a) 3")

# Fig 4
# - Law of symmetry
# - Law of 


######################
# b)
######################

# Fig 1
pcount = 50
xs = [math.sin(x*math.pi*2.0*random.random()) for x in range(pcount)]
ys = [math.cos(x*math.pi*2.0*random.random()) for x in range(pcount)]
axes[2].scatter(xs, ys, marker='.', color=colors[2 % len(colors)])
axes[2].set_title("b) 1")

# Fig 2


# Fig 3
#rnd = lambda: random.random() * 2 - 1
pcount = 100
rnd = np.random.normal(0, .5, (2, pcount))
axes[3].scatter(rnd[0], rnd[1], marker='.', color=colors[3 % len(colors)])
axes[3].set_title("b) 3")

plt.tight_layout()
plt.savefig("2.1.pdf")
plt.show()