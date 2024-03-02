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


if __name__ == "__main__":
    draw()
