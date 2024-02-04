import matplotlib.pyplot as plt
import numpy as np


def first_connection():
    labels = ['client2gateway', 'gateway2swarm', 'functionExec', 'function2client']
    x86_data = [22.92, 11.96, 0.10, 1.74]
    riscv64_data = [45.29, 8.07, 0.48, 18.66]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, x86_data, width, label='x86')
    ax.bar(x + width / 2, riscv64_data, width, label='riscv64')

    # 添加标签、标题和图例
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('time(ms)')
    ax.set_title('First Connection(With payload)')
    ax.legend()

    plt.show()

def first_second():
    labels = ['x86', 'riscv64']
    first_data = [36.72, 72.5]
    second_data = [2.71, 5.76]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, first_data, width, label='first')
    ax.bar(x + width / 2, second_data, width, label='second')

    # 添加标签、标题和图例
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('time(ms)')
    ax.set_title('First vs Second')
    ax.legend()

    plt.show()


def second_connection():
    labels = ['client2gateway', 'gateway2swarm', 'functionExec', 'function2client']
    x86_data = [0.39, 0.93, 0.028, 1.36]
    riscv64_data = [1.81, 1.97, 0.15, 1.83]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, x86_data, width, label='x86')
    ax.bar(x + width / 2, riscv64_data, width, label='riscv64')

    # 添加标签、标题和图例
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    ax.set_ylim([0, 50])
    # figure.set_ylim(bottom=0, top=50)

    ax.set_ylabel('time(ms)')
    ax.set_title('Connection(With payload)')
    ax.legend()

    plt.show()


if __name__ == '__main__':
    second_connection()
