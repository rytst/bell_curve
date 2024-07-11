import numpy as np
import matplotlib.pyplot as plt


x_means = []
sample_size = [1, 2, 4, 10, 100]



fig, axs = plt.subplots(5, figsize=(25,30))

for (i, N) in enumerate(sample_size):
    for _ in range(10000):
        xs = []
        for n in range(N):
            x = np.random.rand()
            xs.append(x)
        mean = np.mean(xs)
        x_means.append(mean)
    
    
    axs[i].hist(x_means, bins='auto', density=True)
    axs[i].set_title(f'N={N}')
    axs[i].set(xlabel='x', ylabel='Probability Density')
    axs[i].set_xlim(-0.05, 1.05)
    axs[i].set_ylim(0, 5)

fig.savefig(f'sample_avg.png')
