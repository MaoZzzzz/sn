import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 5
    x = np.arange(size)
    # AITurbo = [1194.1, 2266]
    AITurbo2 = [1, 1, 1, 1, 1]
    AITurbo = [1.48, 1.34, 1.24, 1.1, 1]
    Optimus = [2.1, 2.2, 2.5, 3.3, 3.9]
    Tiresias = [5.3, 4.3, 3.9, 3.3, 2.2]
    labels = ['0:100', '25:75', '50:50', '75:25', '100:0']

    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / 5

    plt.figure(figsize=(7, 4))
    plt.gca().spines['bottom'].set_linewidth(2.5)
    plt.gca().spines['left'].set_linewidth(2.5)
    plt.gca().spines['top'].set_linewidth(2.5)
    plt.gca().spines['right'].set_linewidth(2.5)
    plt.bar(x, AITurbo2, width=0.15, label='AITurbo-vGPU', color='brown', linewidth=2.5, edgecolor='black')
    plt.bar(x + (width + 0.01), AITurbo, width=0.15, label='AITurbo', color='red', linewidth=2.5, edgecolor='black')
    plt.bar(x + 2 * (width + 0.01), Optimus, width=0.15, label='Optimus', tick_label=labels, color='black',
            linewidth=2.5, edgecolor='black')
    plt.bar(x + 3 * (width + 0.01), Tiresias, width=0.15, label='Tiresias', color='grey', linewidth=2.5,
            edgecolor='black')
    plt.xlabel('Unpredictable(%):Predictable(%)', fontsize=20)
    plt.ylabel('Norm. Avg. JCT', fontsize=20)
    plt.yticks(size=16)
    plt.xticks(size=16)
    plt.legend(ncol=2, loc=2, bbox_to_anchor=(0.05, 1.15), borderaxespad=0., fontsize=17)
    # plt.legend(loc='upper center')

    y = [0.95, 0.97, 0.98, 0.94, 0.95]
    ax2 = plt.twinx()
    ax2.set_ylabel("Accuracy", fontsize=20)
    plt.yticks(size=16)
    ax2.set_ylim([0.5, 1.0])
    plt.plot(x, y, "r", marker='.', c='r', ms=5, linewidth='1')

    plt.subplots_adjust(bottom=0.2)

    # plt.savefig('predictable.jpg')
    plt.show()
