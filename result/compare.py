import matplotlib.pyplot as plt
import numpy as np


def draw(m, openfaas):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels = ['compose-post', 'upload-creator', 'matmul', 'all time']

    base = [1] * len(m)
    normalized_openfaas = []
    for item in zip(m, openfaas):
        normalized_openfaas.append(item[1] / item[0])
    print(normalized_openfaas)

    width = 0.5
    ind = np.arange(len(labels))

    fig, ax = plt.subplots()
    ax.bar(ind - width / 4, base, width / 2, label='m', edgecolor='black')
    ax.bar(ind + width / 4, normalized_openfaas, width / 2, label='openfaas', edgecolor='black')

    ax.set_xticks(ind)
    ax.set_xticklabels(labels)

    ax.legend()

    plt.ylabel('归一化时间')
    plt.title('对比')
    plt.grid()

    # plt.savefig()
    plt.show()


def periodic():
    m = [11111262, 55114777, 285753543, 1.31934553e12]
    openfaas = [38561738, 59275287, 3950258727, 4.52937798e12]
    draw(m, openfaas)


def bursty():
    m = [8473923, 48768878, 240753293, 1.38317567e12]
    openfaas = [34612443, 60004783, 4006516348, 6.1529673e12]
    draw(m, openfaas)


def sporadic():
    m = [35393129, 90614491, 285753543, 1.01451439e12]
    openfaas = [144448205, 289913566, 3554073972, 1.07758774e12]
    draw(m, openfaas)


if __name__ == "__main__":
    bursty()
