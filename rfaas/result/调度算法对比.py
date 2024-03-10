import matplotlib.pyplot as plt
import numpy as np


def request_success_rate(fcfs, sdf, srtf):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels = ['稀疏型', '阶段型', '突发型']

    width = 0.9
    ind = np.array([0, 2, 4])

    plt.figure(figsize=(4, 3))

    # plt.bar(ind - (width * 2) / 3, fcfs, (width * 2) / 3, label='FCFS', edgecolor='black')
    # plt.bar(ind, sdf, (width * 2) / 3, label='SDF', edgecolor='black')
    # plt.bar(ind + (width * 2) / 3, srtf, (width * 2) / 3, label='SRTF', edgecolor='black')

    plt.plot(ind, fcfs, marker='*', label='FCFS', linewidth=2)
    plt.plot(ind, sdf, marker='o', label='SDF', linewidth=2)
    plt.plot(ind, srtf, marker='*', label='SRTF', linewidth=2)

    plt.xticks(ind, labels, rotation=0)
    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)

    plt.legend(fontsize=8)
    plt.xlabel('负载类型')
    plt.ylabel('请求成功率', labelpad=5)
    # plt.title('CPU test')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig("request_success_rate.pdf")

    plt.show()


def number_successful_requests(fcfs, sdf, srtf):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels = ['稀疏型', '阶段型', '突发型']

    width = 0.9
    ind = np.array([0, 2, 4])

    plt.figure(figsize=(4, 3))

    plt.bar(ind - (width * 2) / 3, fcfs, (width * 2) / 3, label='FCFS', edgecolor='black')
    plt.bar(ind, sdf, (width * 2) / 3, label='SDF', edgecolor='black')
    plt.bar(ind + (width * 2) / 3, srtf, (width * 2) / 3, label='SRTF', edgecolor='black')

    plt.xticks(ind, labels, rotation=0)
    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)

    plt.legend(fontsize=8)
    plt.xlabel('负载类型')
    plt.ylabel('请求成功数量', labelpad=5)
    # plt.title('CPU test')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig("number_successful_requests.pdf")

    plt.show()


if __name__ == "__main__":
    # Sporadic = [72.34, 76.60, 74.46]
    # Periodic = [14.96, 39.81, 46.15]
    # Bursty = [5.01, 16.08, 31.61]

    fcfs = [72.34, 14.96, 5.01]
    sdf = [76.60, 39.81, 16.08]
    srtf = [74.46, 46.15, 31.61]
    request_success_rate(fcfs, sdf, srtf)

    fcfs = [34, 404, 9]
    sdf = [36, 1075, 231]
    srtf = [35, 1246, 854]
    # number_successful_requests(fcfs, sdf, srtf)
