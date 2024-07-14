import numpy as np
import matplotlib.pyplot as plt
from multivariate_normal import multivariate_normal


mu = np.array([0.5, -0.2])

cov1 = np.array([[1.0, 0.0],
                 [0.0, 1.0]])

cov2 = np.array([[3.0, 0.0],
                 [0.0, 1.0]])

cov3 = np.array([[1.0, 0.3],
                 [0.3, 1.0]])

cov4 = np.array([[1.0, -0.5],
                 [-0.5, 1.0]])

covs = np.array([cov1, cov2, cov3, cov4])



xs = ys = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(xs, ys)
Z = np.zeros((covs.shape[0], X.shape[0], X.shape[1]))


for idx in range(Z.shape[0]):
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x = np.array([X[i, j], Y[i, j]])
            Z[idx][i, j] = multivariate_normal(x, mu, covs[idx])


# plot
fig = plt.figure(figsize=(10, 10))

for i in range(Z.shape[0]):
    ax = fig.add_subplot(2, 2, i+1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'cov = {covs[i]}')
    ax.contour(X, Y, Z[i])

plt.savefig('cov.png')
