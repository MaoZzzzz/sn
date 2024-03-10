import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 6
    x = np.arange(size)
    # AITurbo = [1194.1, 2266]
    AITurbo2 = [1, 1, 1, 1, 1, 1]
    AITurbo = [1.34, 1.24, 1.2, 1.17, 1.24, 1.24]
    Centralized = [1.24, 1.47, 1.62, 2.65, 3.44, 3.92]
    Optimus = [4.12, 3.94, 3.3, 2.63, 2.32, 1.98]
    labels = ['2', '4', '6', '8', '10', '12']

    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / 3


    plt.bar(x, AITurbo2, width=width, label='AITurbo-vGPU', color='brown', linewidth=0.5, edgecolor='black')
    plt.bar(x + (width + 0.02), AITurbo, width=width, label='AITurbo', color='red', linewidth=0.5, edgecolor='black')
    plt.bar(x + 2 * (width + 0.02), Centralized, width=width, label='Centralized', tick_label=labels, color='black',
            linewidth=0.5, edgecolor='black')
    plt.bar(x + 3 * (width + 0.02), Optimus, width=width, label='Optimus', color='grey', linewidth=0.5,
            edgecolor='black')
    plt.xlabel('Average # of PSes/workers')
    plt.ylabel('Norm. Avg. JCT')
    plt.subplots_adjust(left=0.15, bottom=0.2)
    plt.legend(loc='best')
    plt.savefig('PSes_workers.jpg')
    plt.show()
