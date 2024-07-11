import numpy as np
import matplotlib.pyplot as plt


# normal distribution
def normal(x, mu=0, sigma=1):
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(- (x - mu)**2 / (2 * sigma**2))
    return y


x = np.linspace(-5, 5, 101)

# mapping
y = normal(x)


# plot normal distribution
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('norm_dist.png')
