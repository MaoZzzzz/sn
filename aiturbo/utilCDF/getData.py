import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

data1 = []
data2 = []
data3 = []
data4 = []


def read1() -> None:
    filepath = "D:\\Workdir\\实验数据\\gpu-high\\optimus"
    filefullpath = filepath + "\\" + "1.txt"
    d1 = []
    d2 = []
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d1.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d1[len(d1) - 1] = (d1[len(d1) - 1] + float(line[4])) / 2
    filefullpath = filepath + "\\" + "2.txt"
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d2.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d2[len(d2) - 1] = (d2[len(d2) - 1] + float(line[4])) / 2

    for i in range(len(d1)):
        data1.append((d1[i] + d2[i]) / 2)


def read2() -> None:
    filepath = "D:\\Workdir\\实验数据\\gpu-high\\tresias"
    filefullpath = filepath + "\\" + "1.txt"
    d1 = []
    d2 = []
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d1.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d1[len(d1) - 1] = (d1[len(d1) - 1] + float(line[4])) / 2
    filefullpath = filepath + "\\" + "2.txt"
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d2.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d2[len(d2) - 1] = (d2[len(d2) - 1] + float(line[4])) / 2

    for i in range(len(d1)):
        data2.append((d1[i] + d2[i]) / 2)


def read3() -> None:
    filepath = "D:\\Workdir\\实验数据\\gpu-high\\aiturbo"
    filefullpath = filepath + "\\" + "1.txt"
    d1 = []
    d2 = []
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d1.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d1[len(d1) - 1] = (d1[len(d1) - 1] + float(line[4])) / 2
    filefullpath = filepath + "\\" + "2.txt"
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d2.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d2[len(d2) - 1] = (d2[len(d2) - 1] + float(line[4])) / 2

    for i in range(len(d1)):
        data3.append((d1[i] + d2[i]) / 2)


def read4() -> None:
    filepath = "D:\\Workdir\\实验数据\\gpu-high\\vgpu"
    filefullpath = filepath + "\\" + "1.txt"
    d1 = []
    d2 = []
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d1.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d1[len(d1) - 1] = (d1[len(d1) - 1] + float(line[4])) / 2

    filefullpath = filepath + "\\" + "2.txt"
    with open(filefullpath, 'r') as f:
        count = len(open(filefullpath, 'rU').readlines())
        for i in range(count):
            line = f.readline().split(" ")
            line = list(filter(None, line))
            if len(line) > 0:
                line[len(line) - 1] = line[len(line) - 1][:-1]
                if line[4].isdigit() and line[0] == '0':
                    d2.append(float(line[4]))
                if line[4].isdigit() and line[0] == '1':
                    d2[len(d2) - 1] = (d2[len(d2) - 1] + float(line[4])) / 2

    for i in range(len(d1)):
        data4.append((d1[i] + d2[i]) / 2)


def drawcdf():
    ecdf1 = sm.distributions.ECDF(data1)
    ecdf2 = sm.distributions.ECDF(data2)
    ecdf3 = sm.distributions.ECDF(data3)
    ecdf4 = sm.distributions.ECDF(data4)
    # 等差数列，用于绘制X轴数据
    x1 = np.linspace(min(data1), max(data1))
    x2 = np.linspace(min(data2), max(data2))
    x3 = np.linspace(min(data3), max(data3))
    x4 = np.linspace(min(data3), max(data4))
    # x轴数据上值对应的累计密度概率
    y1 = ecdf1(x1)
    y2 = ecdf2(x2)
    y3 = ecdf3(x3)
    y4 = ecdf4(x4)
    # 绘制阶梯图
    with plt.style.context(['ieee', 'grid']):
        plt.figure(figsize=(3.8, 2.85))

        plt.gca().spines['bottom'].set_linewidth(1.1)
        plt.gca().spines['left'].set_linewidth(1.1)
        plt.gca().spines['top'].set_linewidth(1.1)
        plt.gca().spines['right'].set_linewidth(1.1)

        plt.plot(x1, y1, "black", linewidth='1.8', linestyle='-', label='Optimus')
        plt.plot(x2, y2, "black", linewidth='1.8', linestyle='-.', label='Tiresias')
        plt.plot(x3, y3, "red", linewidth='1.8', linestyle='-', label='AITurbo')
        plt.plot(x4, y4, "brown", linewidth='1.8', linestyle='-', label='AITurbo-vGPU')
        plt.xlabel('Utilization(%)', fontdict={'size': 15})
        plt.ylabel('CDF', fontdict={'size': 15})
        plt.tick_params(labelsize=15, direction='in')

        plt.subplots_adjust(left=0.2, bottom=0.2)

        # plt.legend(bbox_to_anchor=(-0.03, 1.03), labelspacing=0.1, borderpad=0.1, loc="lower right", fontsize=13, edgecolor='black', framealpha=0.66)
        plt.legend(loc="upper left", handletextpad=0.1, fontsize=12, edgecolor='black', framealpha=0.6, labelspacing=0.1, borderpad=0.1, fancybox=False)

        plt.xlim((0, 100))
        ax = plt.gca()
        x_major_locator = MultipleLocator(20)
        ax.xaxis.set_major_locator(x_major_locator)

        ax.set_ylim([0, 1])
        ymajorLocator = MultipleLocator(0.2)
        ax.yaxis.set_major_locator(ymajorLocator)

        plt.grid(b=None)
        plt.tight_layout()
        plt.savefig('gpu_util_high.eps')
        plt.show()


if __name__ == '__main__':
    read1()
    read2()
    read3()
    read4()
    drawcdf()
