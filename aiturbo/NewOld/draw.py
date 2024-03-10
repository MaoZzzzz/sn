import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 3
    x = np.arange(size)
    # AITurbo = [1194.1, 2266]
    AITurbo2 = [1, 1, 1]
    AITurbo = [1.24, 1.24, 1.24]
    Optimus = [2.2, 2.6, 2.65]
    Tiresias = [3.8, 3.6, 3.5]
    labels = ['25:75', '50:50', '75:25']

    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / 3

    plt.figure(figsize=(5, 4))
    plt.gca().spines['bottom'].set_linewidth(2.5)
    plt.gca().spines['left'].set_linewidth(2.5)
    plt.gca().spines['top'].set_linewidth(2.5)
    plt.gca().spines['right'].set_linewidth(2.5)
    plt.bar(x, AITurbo2, width=width, label='AITurbo-vGPU', color='brown', linewidth=2.5, edgecolor='black')
    plt.bar(x + (width + 0.02), AITurbo, width=width, label='AITurbo', color='red', linewidth=2.5, edgecolor='black')
    plt.bar(x + 2 * (width + 0.02), Optimus, width=width, label='Optimus', tick_label=labels, color='black',
            linewidth=2.5, edgecolor='black')
    plt.bar(x + 3 * (width + 0.02), Tiresias, width=width, label='Tiresias', color='grey', linewidth=2.5,
            edgecolor='black')
    plt.xlabel('New jobs(%):Old jobs(%)', fontsize=20)
    plt.ylabel('Norm. Avg. JCT', fontsize=20)
    plt.yticks(size=16)
    plt.xticks(size=16)
    plt.subplots_adjust(bottom=0.2, left=0.2)
    plt.legend(ncol=2, loc=2, bbox_to_anchor=(-0.1, 1.20), borderaxespad=0., fontsize=16)
    plt.savefig('NewOld.jpg')
    plt.show()
