from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']


def ps_worker_jct():
    AITurbo2 = [1, 1, 1, 1, 1, 1]
    AITurbo = [1.24, 1.24, 1.2, 1.17, 1.24, 1.24]
    Centralized = [1.1, 1.47, 1.62, 2.65, 3.44, 3.92]
    Optimus = [4.12, 3.94, 3.3, 2.63, 2.32, 1.98]
    labels = ['2', '4', '6', '8', '10', '12']

    plt.figure(figsize=(5, 3))

    bar_width = 0.4
    x = np.arange(len(labels)) * 2

    p1 = plt.bar(x - 3 * bar_width / 2, AITurbo2, width=bar_width, align='center', edgecolor='black')
    p2 = plt.bar(x - bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black')
    p3 = plt.bar(x + bar_width / 2, Centralized, width=bar_width, align='center', edgecolor='black')
    p4 = plt.bar(x + 3 * bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black')

    plt.ylabel('归一化时间', fontdict={'family': 'SimSun', 'size': 13})
    # plt.xlabel('参数服务器和', fontdict={'size': 16})
    plt.tick_params(labelsize=13)
    plt.grid()
    plt.margins(0)

    plt.xticks(x, labels)

    # plt.tight_layout()
    plt.subplots_adjust(bottom=0.23)
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Weaver', 'AITurbo', 'Centralized', 'Optimus'), loc='upper left',
               fontsize=13)

    plt.savefig('ps_worker_jct.pdf')
    plt.show()


def small_large_jct():
    AITurbo2 = [1, 1, 1, 1, 1]
    AITurbo = [1.34, 1.24, 1.2, 1.17, 1.24]
    Centralized = [1.24, 1.47, 2.12, 2.65, 3.44]
    Optimus = [1.12, 1.94, 1.83, 1.73, 1.32]
    labels = ['100:0', '75:25', '50:50', '25:75', '0:100']

    plt.figure(figsize=(5, 3))

    bar_width = 0.4
    x = np.arange(len(labels)) * 2

    p1 = plt.bar(x - 3 * bar_width / 2, AITurbo2, width=bar_width, align='center', edgecolor='black')
    p2 = plt.bar(x - bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black')
    p3 = plt.bar(x + bar_width / 2, Centralized, width=bar_width, align='center', edgecolor='black')
    p4 = plt.bar(x + 3 * bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black')

    plt.ylabel('归一化时间', fontdict={'family': 'SimSun', 'size': 13})
    # plt.xlabel('Small(%):Large(%)', fontdict={'size': 13})
    plt.tick_params(labelsize=13)
    plt.grid()
    plt.margins(0)

    plt.xticks(x, labels)
    # plt.tight_layout()
    plt.subplots_adjust(bottom=0.23)
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Weaver', 'AITurbo', 'Centralized', 'Optimus'), loc='upper left',
               fontsize=13)

    plt.savefig('small_large_jct.pdf')
    plt.show()


if __name__ == '__main__':
    ps_worker_jct()
