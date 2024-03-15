from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']


def overall_jct():
    labels = ['平均完成时间', '整体完成时间']

    AITurbo_vGPU = [1, 1]
    AITurbo = [1.24, 1.34]
    Optimus = [1.8, 2.1]
    Tiresias = [2.8, 3.394]
    SRTF = [1.9, 4.694]
    FCFS = [4.2, 3.394]

    plt.figure(figsize=(4, 2))
    bar_width = 0.3
    x = np.arange(len(labels)) * 2

    plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
    plt.bar(x - 3 * bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
    plt.bar(x - bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + 3 * bar_width / 2, SRTF, color='lightgrey', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + 5 * bar_width / 2, FCFS, color='white', width=bar_width, align='center', edgecolor='black')

    plt.xticks(x, labels)

    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)

    # plt.legend(fontsize=8)
    plt.ylabel('归一化时间', labelpad=5, fontsize=13)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.savefig("overall_jct.pdf")
    plt.show()


def long_short_jct():
    labels = ['短期作业', '长期作业']

    AITurbo_vGPU = [1, 1]
    AITurbo = [1.24, 1.14]
    Optimus = [4.1, 2.9]
    Tiresias = [3.1, 3.9]
    SRTF = [2.1, 3.6]
    FCFS = [8, 3.9]

    plt.figure(figsize=(4, 2))

    bar_width = 0.3
    x = np.arange(len(labels)) * 2

    plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
    plt.bar(x - 3 * bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
    plt.bar(x - bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + 3 * bar_width / 2, SRTF, color='lightgrey', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + 5 * bar_width / 2, FCFS, color='white', width=bar_width, align='center', edgecolor='black')

    plt.xticks(x, labels)

    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)

    # plt.legend(fontsize=8)
    plt.ylabel('归一化时间', labelpad=5, fontsize=13)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.savefig("long_short_jct.pdf")
    plt.show()


if __name__ == '__main__':
    overall_jct()
