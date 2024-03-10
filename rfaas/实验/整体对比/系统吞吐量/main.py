import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']


def draw():
    openfaas = [0.1, 0.27, 0.27]
    rfaas_wo_sysytemcall = [0.41, 1.43, 1.21]
    rfaas = [0.42, 1.64, 1.61]
    labels = ["稀疏型", "阶段型", "突发型"]

    base = [1] * len(openfaas)
    normalized_rfaas_wo_sysytemcall = []
    normalized_rfaas = []
    for item in zip(openfaas, rfaas_wo_sysytemcall, rfaas):
        normalized_rfaas_wo_sysytemcall.append(item[1] / item[0])
        normalized_rfaas.append(item[2] / item[0])

    plt.figure(figsize=(6, 3))
    bar_width = 0.5
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.bar(ind - bar_width / 2, base, bar_width / 2, alpha=opacity, label='OpenFaas', edgecolor='black')
    plt.bar(ind, normalized_rfaas_wo_sysytemcall, bar_width / 2, alpha=opacity, label='RFaas-',
            edgecolor='black')
    plt.bar(ind + bar_width / 2, normalized_rfaas, bar_width / 2, alpha=opacity, label='RFaas', edgecolor='black')

    for i, value in enumerate(rfaas):
        plt.text(ind[i] - bar_width / 2, base[i], str(value), ha='center', va='bottom', fontsize=10)
    for i, value in enumerate(rfaas_wo_sysytemcall):
        plt.text(ind[i], normalized_rfaas_wo_sysytemcall[i], str(value), ha='center', va='bottom', fontsize=10)
    for i, value in enumerate(rfaas):
        plt.text(ind[i] + bar_width / 2, normalized_rfaas[i], str(value), ha='center', va='bottom', fontsize=10)

    plt.xticks(ind, labels)
    plt.tick_params(axis='both', which='major', labelsize=10, length=0)
    plt.margins(x=0)

    plt.legend(fontsize=10)
    plt.ylabel('归一化结果', labelpad=5)
    plt.grid(True, linestyle='--')
    # plt.subplots_adjust(bottom=0.4)
    plt.savefig("throughput_compare.pdf")
    plt.show()


if __name__ == "__main__":
    draw()
