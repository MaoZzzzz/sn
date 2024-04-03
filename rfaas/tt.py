import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False


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


def draw_in_one():
    fig, axs = plt.subplots(1, 2, figsize=(6, 2))

    labels = ['C2G', 'G2S', 'FExec', 'F2C']

    first_x86_data = [22.92, 7.96, 0.10, 1.74]
    first_riscv64_data = [45.29, 8.07, 0.48, 2.3]

    second_x86_data = [0.39, 0.93, 0.028, 1.36]
    second_riscv64_data = [1.81, 1.97, 0.15, 1.83]

    x = np.arange(len(labels))
    width = 0.4

    legend_font = {"family": "Times New Roman"}

    ax0 = axs[0]
    ax0.bar(x - width / 2, first_x86_data, width, label='X86', edgecolor='black')
    ax0.bar(x + width / 2, first_riscv64_data, width, label='RISCV', edgecolor='black')
    ax0.set_xticks(x)
    ax0.set_xticklabels(labels, fontsize=10)
    ax0.set_ylabel('时间(ms)', fontsize=10, fontproperties='SimSun')
    # ax0.set_xlabel('阶段')
    ax0.set_title('第一次连接时间示例', fontsize=10, fontproperties='SimSun')
    ax0.set_ylim([0, 50])
    ax0.legend(fontsize=10, prop=legend_font)

    ax1 = axs[1]
    ax1.bar(x - width / 2, second_x86_data, width, label='X86', edgecolor='black')
    ax1.bar(x + width / 2, second_riscv64_data, width, label='RISCV', edgecolor='black')
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=10)
    ax1.set_title('第二次连接时间示例', fontsize=10, fontproperties='SimSun')
    ax1.set_ylim([0, 50])
    ax1.legend(fontsize=10, prop=legend_font)

    # plt.subplots_adjust(wspace=0.25, bottom=0.2)
    plt.savefig("two_stage_connect_time_compare.pdf")
    plt.tight_layout()
    plt.show()


def first_second():
    labels = ['x86', 'riscv64']
    first_data = [36.72, 72.5]
    second_data = [2.71, 5.76]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(6, 2))
    ax.bar(x - width / 2, first_data, width, label='first')
    ax.bar(x + width / 2, second_data, width, label='second')

    # 添加标签、标题和图例
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('time(ms)')
    ax.set_title('First vs Second')
    ax.legend()

    plt.show()


if __name__ == '__main__':
    draw_in_one()
