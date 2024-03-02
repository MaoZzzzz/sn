import matplotlib.pyplot as plt
import numpy as np


def draw(KNN, RFR, SVR, MLP, LR):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels = ['准确度', '精度', '召回率', 'F1分数']

    size = 4
    x = np.arange(size)

    total_width, n = 1.0, 6
    width = total_width / n
    x = x - (total_width - width) / 2

    fig, ax = plt.subplots()
    ax.bar(x, KNN, width, label='KNN', edgecolor='black')
    ax.bar(x + width, RFR, width, label='RFR', edgecolor='black')
    ax.bar(x + width * 2, SVR, width, label='SVR', edgecolor='black')
    ax.bar(x + width * 3, MLP, width, label='MLP', edgecolor='black')
    ax.bar(x + width * 4, LR, width, label='LR', edgecolor='black')

    ax.set_xticks(x + width * 2)
    ax.set_xticklabels(labels)

    ax.legend()

    # plt.ylabel('归一化时间')
    plt.title('对比')
    plt.grid()

    # plt.savefig()
    plt.show()


def periodic():
    KNN = [95.24, 97.62, 93.18, 95.35]
    RFR = [95.24, 99.70, 90.91, 95.24]
    SVR = [91.67, 92.91, 91.67, 91.64]
    MLP = [91.67, 92.90, 91.67, 91.62]
    LR = [89.29, 91.25, 89.28, 89.21]
    draw(KNN, RFR, SVR, MLP, LR)


if __name__ == "__main__":
    periodic()
