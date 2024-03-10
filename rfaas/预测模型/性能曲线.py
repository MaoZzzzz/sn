import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def exponential_func(x, a, b):
    return a * np.exp(b * x)


def linear_func(x, a, b):
    return a * x + b


def quadratic_func(x, a, b, c):
    return a * x ** 2 + b * x + c


def logarithmic_func(x, a, b):
    return a * np.log(x) + b


def draw_scatter(path):
    x, y = [], []
    with open(path, 'r') as file:
        for line in file:
            values = line.split()
            if float(values[1]) * 1000 > 10:
                values[1] = 6 / 1000
            elif float(values[1]) * 1000 > 2:
                values[1] = float(values[1]) / 5000
            x.append(float(values[0]))
            y.append(float(values[1]) * 1000)

    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    plt.figure(figsize=(4, 3))

    popt, pcov = curve_fit(quadratic_func, x, y)
    fit_y = quadratic_func(x, *popt)

    plt.scatter(x, y, s=20, edgecolors='black')
    plt.plot(x, fit_y, 'r', linewidth=2)

    # plt.xticks(ind, labels, rotation=0)
    # plt.legend(fontsize=8)
    plt.xlabel('负载大小(bytes)')
    plt.ylabel('执行时间(ms)')

    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.savefig("compose_post_curve_x86.pdf")

    plt.show()


def draw_scatter_matmul(path):
    x, y = [], []
    with open(path, 'r') as file:
        for line in file:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))

    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    plt.figure(figsize=(4, 3))

    popt, pcov = curve_fit(quadratic_func, x, y)
    fit_y = quadratic_func(x, *popt)

    plt.scatter(x, y, s=20, edgecolors='black')
    plt.plot(x, fit_y, 'r', linewidth=2)

    # plt.xticks(ind, labels, rotation=0)
    # plt.legend(fontsize=8)
    plt.xlabel('矩阵维度')
    plt.ylabel('执行时间(ms)')

    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.savefig("matmul_curve_riscv.pdf")

    plt.show()


def draw(path):
    x, y = [], []
    with open(path, 'r') as file:
        for line in file:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))

    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    fig, axs = plt.subplots(1, 3, figsize=(9, 2))

    ax0 = axs[0]
    popt, pcov = curve_fit(quadratic_func, x, y)
    fit_y = quadratic_func(x, *popt)

    ax0.scatter(x, y, s=20, edgecolors='black')
    ax0.plot(x, fit_y, 'r', linewidth=2)

    ax0.set_xlabel('负载大小(bytes)', fontsize=10)
    ax0.set_ylabel('执行时间(ms)', fontsize=10)
    ax0.set_title('二次函数拟合', fontsize=10)

    ax0.grid(True, linestyle='--')

    ax1 = axs[1]
    popt, pcov = curve_fit(linear_func, x, y)
    fit_y = linear_func(x, *popt)

    ax1.scatter(x, y, s=20, edgecolors='black')
    ax1.plot(x, fit_y, 'r', linewidth=2)

    ax1.set_xlabel('负载大小(bytes)', fontsize=10)
    ax1.set_title('线性函数拟合', fontsize=10)

    ax1.grid(True, linestyle='--')

    ax2 = axs[2]
    popt, pcov = curve_fit(logarithmic_func, x, y, maxfev=200000)
    fit_y = logarithmic_func(x, *popt)

    ax2.scatter(x, y, s=20, edgecolors='black')
    ax2.plot(x, fit_y, 'r', linewidth=2)

    ax2.set_xlabel('负载大小(bytes)', fontsize=10)
    ax2.set_title('对数函数拟合', fontsize=10)

    ax2.grid(True, linestyle='--')

    plt.subplots_adjust(wspace=0.25, bottom=0.2)
    plt.savefig("three_curve_function_compare_compose_post.pdf")
    plt.show()


if __name__ == "__main__":
    draw("D:\Workdir\idea\Schedule\data\predictResult\compose-post.txt")
