import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 1
    x = np.arange(size)
    # MPS = [1568, 3600]
    # MPS(1/4) = [1596, 3749]
    # MPS(1/8) = [1586, 3799]
    MPS = 1
    AITurbo = 1.51
    Optimus = 2.1616

    data = [MPS, AITurbo, Optimus]
    labels = ['MPS', 'AITurbo', 'Optimus']

    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 1

    plt.ylabel('Norm.Avg.JCT')

    plt.bar(range(len(data)), data, tick_label=labels, color='rgb')
    plt.legend()
    plt.show()
