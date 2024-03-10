import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    size = 2
    x = np.arange(size)
    # AITurbo = [1194.1, 2266]
    AITurbo2 = [1, 1]
    AITurbo = [1.24, 1.34]
    Optimus = [1.8, 2.1]
    Tiresias = [2.8, 3.394]
    SRTF = [1.9, 4.694]
    FCFS = [4.2, 3.394]
    labels = ['JCT', 'makespan']

    total_width, n = 0.8, 6
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.gca().spines['bottom'].set_linewidth(1.5)
    plt.gca().spines['left'].set_linewidth(1.5)
    plt.gca().spines['top'].set_linewidth(1.5)
    plt.gca().spines['right'].set_linewidth(1.5)
    plt.bar(x, AITurbo2, width=width, label='AITurbo-vGPU', color='brown', linewidth=1.5, edgecolor='black')
    plt.bar(x + (width + 0.02), AITurbo, width=width, label='AITurbo', color='red', linewidth=1.5, edgecolor='black')
    plt.bar(x + 2 * (width + 0.02), Optimus, width=width, label='Optimus', tick_label=labels, color='black',
            linewidth=1.5, edgecolor='black')
    plt.bar(x + 3 * (width + 0.02), Tiresias, width=width, label='Tiresias', color='grey', linewidth=1.5,
            edgecolor='black')
    plt.bar(x + 4 * (width + 0.02), SRTF, width=width, label='SRTF', color='lightgrey', linewidth=1.5,
            edgecolor='black')
    plt.bar(x + 5 * (width + 0.02), FCFS, width=width, label='FCFS', color='white', linewidth=1.5, edgecolor='black')
    # plt.xlabel('Unpredictable(%):Predictable(%)')
    plt.ylabel('Norm. Avg. JCT', fontsize=14)
    plt.yticks(size=14)
    plt.xticks(size=14)
    plt.subplots_adjust(left=0.2, bottom=0.2)
    # plt.legend(ncol=3, loc='best', borderaxespad=0.)
    plt.legend(ncol=3, loc=2, bbox_to_anchor=(-0.25, 1.15), borderaxespad=0., fontsize=8)
    plt.savefig('Overall comparison.jpg')
    plt.show()
