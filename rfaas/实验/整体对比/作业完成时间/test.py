import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']

file_path = 'data.txt'


def draw(rfaas, openfaas):
    labels = ['阶段型', '突发型', '稀疏型']

    base = [1] * len(rfaas)
    normalized_openfaas = []
    for item in zip(rfaas, openfaas):
        normalized_openfaas.append(item[1] / item[0])

    plt.figure(figsize=(4, 3))
    bar_width = 0.6
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.bar(ind - bar_width / 4, base, bar_width / 2, alpha=opacity, label='RFaaS', edgecolor='black')
    plt.bar(ind + bar_width / 4, normalized_openfaas, bar_width / 2, alpha=opacity, label='OpenFaaS', edgecolor='black')

    plt.xticks(ind, labels)
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)

    plt.legend(fontsize=13, loc='upper left')
    plt.ylabel('归一化结果', labelpad=5, fontsize=13)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.3, left=0.2)
    plt.savefig("openfaas_RFaas_full_time_compare.pdf")
    plt.show()


if __name__ == "__main__":
    rfaas = [1, 1, 1]
    openfaas = [3.34, 4.65, 1.03]
    draw(rfaas, openfaas)
