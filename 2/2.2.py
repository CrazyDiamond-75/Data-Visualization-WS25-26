import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.simpledialog import askstring
from random import shuffle


def game(num_static, num_random, iteration):
    dfs = []
    dfs.append(pd.DataFrame(np.random.random_sample(size=(num_static, 2)), columns=['x', 'y']))
    dr = pd.DataFrame(np.random.random_sample(size=(num_random, 2)), columns=['x', 'y'])
    dfs.append(pd.concat([dfs[0], dr]))

    index = [0,1]
    shuffle(index)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)
    axes = axes.flatten()

    i = index[0]
    
    axes[0].scatter(dfs[i]['x'], dfs[i]['y'], marker='.')
    axes[0].set_title('A')
    
    i = index[1]

    axes[1].scatter(dfs[i]['x'], dfs[i]['y'], marker='.')
    axes[1].set_title('B')

    plt.tight_layout()
    fig.canvas.manager.set_window_title(f'Round {iteration}')
    plt.show()

    res = askstring(f'Round {iteration}', 'Which image contained more points?')
    
    if res not in ['A', 'B']:
        return None
    
    answer = {'A': 0, 'B': 1}[res]
    solution = int(index[1] == 1) # Position of plot with more points.
    return answer == solution


def main():
    iteration = 0
    score = 0
    while iteration < 10:
        print(f'Round: {iteration}\tScore: {score}')
        iteration += 1
        result = game(10 + iteration * 10, 10 - iteration, iteration)
        if result is None:
            break
        score += result
    print(f'Game Over!\nScore: {score}')
    return 0

if __name__=="__main__":
    main()
