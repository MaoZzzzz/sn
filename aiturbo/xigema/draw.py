import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    jct = [1.283, 1.091, 1.000, 1.039, 1.134, 1.474]

    labels = ['1', '5', '10', '15', '20', '40']
    y = np.array(list(labels))

    plt.figure(figsize=(10, 10))
    plt.gca().spines['bottom'].set_linewidth(3)
    plt.gca().spines['left'].set_linewidth(3)
    plt.gca().spines['top'].set_linewidth(3)
    plt.gca().spines['right'].set_linewidth(3)

    plt.bar(range(len(jct)), jct, width=0.5, color='black', linewidth=0.5, edgecolor='black', tick_label=labels)
    plt.xlabel("GPU/CPU", size=24)
    plt.ylabel("Norm. Avg JCT", size=24)
    plt.yticks(fontproperties='Times New Roman', size=24, weight='bold')
    plt.xticks(fontproperties='Times New Roman', size=24, weight='bold')

    for a, b in zip(range(len(jct)), jct):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=17)
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.savefig('Impact_of_xigema.jpg')
    plt.show()
