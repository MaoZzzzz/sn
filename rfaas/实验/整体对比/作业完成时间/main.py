import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']


def draw(rfaas, rfaas_wo_sysytemcall, openfaas):
    # labels = ['compose-post', 'upload-creator', 'upload-user-mentions', 'upload-text', 'upload-media',
    #           'upload-unique-id', 'compose-and-upload', 'post-storage', 'upload-user-timeline', 'upload-home-timeline',
    #           'matmul', 'float', 'dd', 'json']

    labels = ['CP', 'UC', 'UUM', 'UT', 'UM', 'UUI', 'CAU', 'PS', 'UUT', 'UHT', 'mat.', 'float', 'dd', 'json']

    base = [1] * len(rfaas)
    normalized_rfaas_wo_sysytemcall = []
    normalized_openfaas = []
    for item in zip(rfaas, rfaas_wo_sysytemcall, openfaas):
        normalized_rfaas_wo_sysytemcall.append(item[1] / item[0])
        normalized_openfaas.append(item[2] / item[0])

    plt.figure(figsize=(8, 2))
    bar_width = 0.6
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.bar(ind - bar_width / 2, base, bar_width / 2, alpha=opacity, label='RFaas', edgecolor='black')
    plt.bar(ind, normalized_rfaas_wo_sysytemcall, bar_width / 2, alpha=opacity, label='RFaas-',
            edgecolor='black')
    plt.bar(ind + bar_width / 2, normalized_openfaas, bar_width / 2, alpha=opacity, label='OpenFaas', edgecolor='black')

    plt.xticks(ind, labels)
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)
    plt.ylim(0, 20)

    plt.legend(fontsize=13)
    plt.ylabel('归一化结果', labelpad=5, fontsize=13)
    plt.grid(True, linestyle='--')
    # plt.subplots_adjust(bottom=0.4)
    plt.savefig("periodic_compare.pdf")
    plt.show()


def sporadic():
    rfaas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    rfaas_wo_sysytemcall = [1.081, 1.002, 1.000, 1.032, 0.998, 0.989, 1.237, 1.276, 1.198, 1.289, 1.213, 1.298, 1.001,
                            1.003]
    openfaas = [4.258, 2.657, 2.345, 3.973, 4.322, 5.236, 4.556, 2.389, 2.198, 2.289, 13.235, 9.298, 1.454, 1.932]
    draw(rfaas, rfaas_wo_sysytemcall, openfaas)


def periodic():
    rfaas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    rfaas_wo_sysytemcall = [1.072, 1.326, 1.192, 1.082, 1.092, 1.004, 1.064, 1.296, 2.138, 2.289, 7.783, 4.923, 1.078,
                            1.032]
    openfaas = [5.952, 3.325, 3.231, 4.973, 5.372, 7.224, 7.742, 4.389, 3.083, 4.289, 15.598, 10.928, 2.354, 2.832]
    draw(rfaas, rfaas_wo_sysytemcall, openfaas)


def bursty():
    rfaas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    rfaas_wo_sysytemcall = [1.184, 1.793, 1.693, 1.539, 2.372, 2.254, 2.029, 2.196, 2.328, 2.892, 12.783, 7.923, 1.098,
                            1.322]
    openfaas = [7.492, 3.983, 3.735, 8.723, 9.749, 9.328, 8.992, 5.399, 4.983, 6.289, 18.598, 12.298, 3.447, 4.832]
    draw(rfaas, rfaas_wo_sysytemcall, openfaas)


if __name__ == "__main__":
    periodic()
