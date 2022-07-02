import numpy as np
import matplotlib.pyplot as plt

def display_sin_graph(x_aixs_label='x', y_aixs_label='y'):
    x = np.arange(0, 4 * np.pi, 0.1)  #domain 0 <= x < 4pi
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel(x_aixs_label)
    plt.ylabel(y_aixs_label)
    plt.grid()                        #グリッドの表示
    plt.show()

def object_graph():
    fig, ax = plt.subplots(2, 1)

    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    w = y + z

    ax[0].plot(x, y, ls='-', label='sin', c='k')
    ax[0].plot(x, z, ls='-', label='cos', c='k')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y, z')
    ax[0].set_xlim(0, 4 * np.pi)
    ax[0].grid()
    ax[0].legend()

    ax[1].plot(x, w, color = 'k', marker = '.')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('w')
    ax[1].set_xlim(0, 4 * np.pi)
    ax[1].grid(ls = ':')

    fig.tight_layout()
