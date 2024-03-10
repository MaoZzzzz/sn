import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    jct = [1.531, 1.022, 1.000, 1.178, 1.421, 1.634]

    labels = ['(5,10)', ' ', '(15,30)', ' ', '(25,50)', ' ']
    y = np.array(list(labels))

    plt.figure(figsize=(10, 10))
    plt.gca().spines['bottom'].set_linewidth(3)
    plt.gca().spines['left'].set_linewidth(3)
    plt.gca().spines['top'].set_linewidth(3)
    plt.gca().spines['right'].set_linewidth(3)

    plt.bar(range(len(jct)), jct, width=0.5, color='black', linewidth=0.5, edgecolor='black', tick_label=labels)
    plt.xlabel("Threshold", size=24)
    plt.ylabel("Norm. Avg JCT", size=24)
    plt.yticks(fontproperties='Times New Roman', size=24, weight='bold')
    plt.xticks(fontproperties='Times New Roman', size=24, weight='bold')

    for a, b in zip(range(len(jct)), jct):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=17)
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.savefig('MLFQ.jpg')
    plt.show()
