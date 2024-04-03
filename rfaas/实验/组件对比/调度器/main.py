import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']


# fcfs. srtf, sdf, rfaas
# 47 2700 2700
def success_ratio():
    rrlb = [0.978, 0.331, 0.228]
    fcfs = [1.0, 0.515, 0.389]
    rfaas = [1.0, 0.724, 0.636]
    # srtf = [1.0, 0.965, 0.847]

    labels = ["稀疏型", "阶段型", "突发型"]

    plt.figure(figsize=(4, 3))
    bar_width = 0.2
    opacity = 0.8

    ind = np.array([1, 1.5, 2])
    # plt.bar(ind - bar_width / 2, rrlb, bar_width / 2, alpha=opacity, label='OpenFaas-RRLB', edgecolor='black')
    # plt.bar(ind, fcfs, bar_width / 2, alpha=opacity, label='OpenFaas-FCFS', edgecolor='black')
    # plt.bar(ind + bar_width / 2, rfaas, bar_width / 2, alpha=opacity, label='AGLBSA', edgecolor='black')
    # plt.bar(ind + bar_width + bar_width / 2, srtf, bar_width, alpha=opacity, label='OpenFaas-SRTF', edgecolor='black')

    plt.plot(ind, rrlb, marker='*', label='OpenFaaS-RRLB', linewidth=2)
    plt.plot(ind, fcfs, marker='o', label='OpenFaaS-FCFS', linewidth=2)
    plt.plot(ind, rfaas, marker='*', label='AGPSA', linewidth=2)

    plt.xticks(ind, labels, fontproperties='SimSun')
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    # plt.margins(x=0.05)

    plt.legend(fontsize=13, loc='lower left')
    plt.ylabel('调度成功率', labelpad=5, fontsize=13, fontproperties='SimSun')
    # plt.xlabel('负载类型', labelpad=5)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.2, bottom=0.3)
    plt.savefig("scheduler_success_ratio.pdf")
    plt.show()


def success_num():
    rrlb = [46, 893, 616]
    fcfs = [47, 1390, 1050]
    rfaas = [47, 1955, 1717]
    # srtf = [1.0, 0.965, 0.847]

    labels = ["稀疏型", "阶段型", "突发型"]

    plt.figure(figsize=(4, 3))
    bar_width = 0.2
    opacity = 0.8

    ind = np.array([1, 1.5, 2])
    plt.bar(ind - bar_width / 2, rrlb, bar_width / 2, alpha=opacity, label='OpenFaaS-RRLB', edgecolor='black')
    plt.bar(ind, fcfs, bar_width / 2, alpha=opacity, label='OpenFaaS-FCFS', edgecolor='black')
    plt.bar(ind + bar_width / 2, rfaas, bar_width / 2, alpha=opacity, label='AGPSA', edgecolor='black')
    # plt.bar(ind + bar_width + bar_width / 2, srtf, bar_width, alpha=opacity, label='OpenFaas-SRTF', edgecolor='black')

    plt.xticks(ind, labels, fontproperties='SimSun')
    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    # plt.margins(x=0.05)

    plt.legend(loc='upper left', fontsize=13)
    plt.ylabel('调度成功数量', labelpad=5, fontsize=13, fontproperties='SimSun')
    # plt.xlabel('负载类型', labelpad=5)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.2, bottom=0.3)
    plt.savefig("scheduler_success_num.pdf")
    plt.show()


def three_trace_examples():
    plt.figure(figsize=(5, 3))

    with open('D:\Workdir\idea\Schedule\data\\trace\Sporadic.txt', 'r') as file:
        sporadic = file.readlines()
    with open('D:\Workdir\idea\Schedule\data\\trace\Periodic.txt', 'r') as file:
        periodic = file.readlines()
    with open('D:\Workdir\idea\Schedule\data\\trace\Bursty.txt', 'r') as file:
        bursty = file.readlines()

    sporadic_float = [float(line.strip()) for line in sporadic]
    periodic_float = [float(line.strip()) for line in periodic]
    bursty_float = [float(line.strip()) for line in bursty]

    plt.plot(range(len(sporadic_float)), sporadic_float, label='稀疏型', linewidth=1.5)
    plt.plot(range(len(periodic_float)), periodic_float, label='阶段型', linewidth=1.5)
    plt.plot(range(len(bursty_float)), bursty_float, label='突发型', linewidth=1.5)
    plt.ylabel('频率', fontsize=13, fontproperties='SimSun')

    # plt.xticks([200, 1000], ['周二，周日'], fontproperties='SimSun')
    # plt.tick_params(axis='both', which='major', labelsize=13, length=0)

    plt.legend(loc='upper right', prop={'family': 'SimSun', 'size': 13})
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.2, bottom=0.3)
    plt.savefig("three_trace_examples.pdf")
    plt.show()


if __name__ == '__main__':
    # success_num()
    three_trace_examples()
