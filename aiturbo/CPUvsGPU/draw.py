import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 2
    x = np.arange(size)
    AITurbo2 = [1, 1]
    AITurbo = [1.34, 1.24]
    Optimus = [2.4, 3.1]
    Tiresias = [3.4, 4.9]
    labels = ['100:0', '75:25']

    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / 2

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
    plt.xlabel('GPU jobs(%):CPU jobs(%)', fontsize=20)
    plt.ylabel('Norm. Avg. JCT', fontsize=20)
    plt.yticks(size=16)
    plt.xticks(size=16)
    plt.subplots_adjust(bottom=0.2, left=0.2)
    plt.legend(ncol=2, loc=2, bbox_to_anchor=(-0.1, 1.20), borderaxespad=0., fontsize=16)
    # plt.legend(loc='upper center')

    plt.savefig('cpu-gpu.jpg')
    plt.show()
