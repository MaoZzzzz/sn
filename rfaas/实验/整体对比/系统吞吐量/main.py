import matplotlib.pyplot as plt
import numpy as np

# openfaas = [0.1, 0.27, 0.27]
# rfaas_wo_sysytemcall = [0.41, 1.43, 1.21]
# rfaas = [0.42, 1.64, 1.61]

plt.rcParams['font.sans-serif'] = ['Times New Roman']


def draw_slo():
    openfaas = [0.17, 0.24, 0.27, 0.35, 0.37]
    rfaas = [0.57, 0.87, 1.0, 1.26, 1.13]
    labels = ["50%", "75%", "99%", "150%", "200%"]

    plt.figure(figsize=(5, 3))
    bar_width = 0.6
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.bar(ind - bar_width / 4, openfaas, bar_width / 2, alpha=opacity, label='OpenFaaS', edgecolor='black')
    plt.bar(ind + bar_width / 4, rfaas, bar_width / 2, alpha=opacity, label='RFaaS', edgecolor='black')

    for i, value in enumerate(openfaas):
        plt.text(ind[i] - bar_width / 4, openfaas[i], str(value), ha='center', va='bottom', fontsize=13)
    for i, value in enumerate(rfaas):
        plt.text(ind[i] + bar_width / 4, rfaas[i], str(value), ha='center', va='bottom', fontsize=13)

    plt.xticks(ind, labels)
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    # plt.margins(x=0)

    plt.ylim(0, 1.4)

    plt.legend(fontsize=13)
    plt.ylabel('归一化结果', labelpad=5, fontsize=13, fontproperties='SimSun')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.2)
    plt.savefig("slo_throughput_compare.pdf")
    plt.show()


def draw():
    openfaas = [0.11, 0.28, 0.27]
    rfaas_wo_sysytemcall = [0.38, 0.89, 0.75]
    rfaas = [0.39, 1.02, 1.0]
    labels = ["稀疏型", "阶段型", "突发型"]

    plt.figure(figsize=(5, 3))
    bar_width = 0.3
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.bar(ind - bar_width / 2, openfaas, bar_width / 2, alpha=opacity, label='OpenFaaS', edgecolor='black')
    plt.bar(ind, rfaas_wo_sysytemcall, bar_width / 2, alpha=opacity, label='RFaaS-',
            edgecolor='black')
    plt.bar(ind + bar_width / 2, rfaas, bar_width / 2, alpha=opacity, label='RFaaS', edgecolor='black')

    for i, value in enumerate(openfaas):
        plt.text(ind[i] - bar_width / 2, openfaas[i], str(value), ha='center', va='bottom', fontsize=13)
    for i, value in enumerate(rfaas_wo_sysytemcall):
        plt.text(ind[i], rfaas_wo_sysytemcall[i], str(value), ha='center', va='bottom', fontsize=13)
    for i, value in enumerate(rfaas):
        plt.text(ind[i] + bar_width / 2, rfaas[i], str(value), ha='center', va='bottom', fontsize=13)

    plt.xticks(ind, labels, fontproperties='SimSun')
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    # plt.margins(x=0)

    plt.ylim(0, 1.10)

    plt.legend(fontsize=13)
    plt.ylabel('归一化结果', labelpad=5, fontsize=13, fontproperties='SimSun')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.2)
    plt.savefig("throughput_compare.pdf")
    plt.show()


if __name__ == "__main__":
    draw_slo()
