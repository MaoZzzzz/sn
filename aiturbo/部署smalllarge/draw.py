import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 5
    x = np.arange(size)
    # AITurbo = [1194.1, 2266]
    AITurbo2 = [1, 1, 1, 1, 1]
    AITurbo = [1.34, 1.24, 1.2, 1.17, 1.24]
    Centralized = [1.24, 1.47, 2.12, 2.65, 3.44]
    Optimus = [1.12, 1.94, 1.83, 1.73, 1.32]
    labels = ['100:0', '75:25', '50:50', '25:75', '0:100']

    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / 3


    plt.bar(x, AITurbo2, width=width, label='AITurbo-vGPU', color='brown', linewidth=0.5, edgecolor='black')
    plt.bar(x + (width + 0.02), AITurbo, width=width, label='AITurbo', color='red', linewidth=0.5, edgecolor='black')
    plt.bar(x + 2 * (width + 0.02), Centralized, width=width, label='Centralized', tick_label=labels, color='black',
            linewidth=0.5, edgecolor='black')
    plt.bar(x + 3 * (width + 0.02), Optimus, width=width, label='Optimus', color='grey', linewidth=0.5,
            edgecolor='black')
    plt.xlabel('Small(%):Large(%)')
    plt.ylabel('Norm. Avg. JCT')
    plt.subplots_adjust(left=0.15, bottom=0.2)
    plt.legend(loc='best')
    plt.savefig('Smalllargejobs.jpg')
    plt.show()
