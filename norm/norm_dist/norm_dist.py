import numpy as np
import matplotlib.pyplot as plt

import sys, os

curr_path = os.path.dirname(__file__)
normal_func_path = os.path.join(curr_path, '..')
sys.path.append(normal_func_path)

from normal import normal



x = np.linspace(-5, 5, 101)

# mapping
y = normal(x)


# plot normal distribution
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('norm_dist.png')
