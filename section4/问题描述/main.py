from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']


def draw():
    labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'AlexNet', 'Inception3', 'Inception4', 'Resnet50',
              'Resnet101', 'Resnet152', 'NasNet', 'Overfeat', 'Trivial', 'MobileNet']
    data = [0.23, 0.29, 0.30, 0.01, 0.05, 0.06, 0.28, 0.48, 0.25, 0.36, 0.52, 0.17, 0.16, 0.01, 0.05]
    for i in range(len(data)):
        data[i] = data[i] * 11

    plt.figure(figsize=(3, 2))
    bar_width = 0.6
    opacity = 0.8

    ind = np.arange(len(labels))
    plt.barh(ind, data, height=bar_width, alpha=opacity, tick_label=labels, edgecolor='black')

    plt.xlim((0, 6))

    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)

    # plt.legend(fontsize=8)
    plt.xlabel('最低所需内存大小（GB）', labelpad=5)
    plt.ylabel('模型名称', labelpad=5)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.3, bottom=0.2)
    plt.savefig("memory_min_usage.pdf")
    plt.show()


if __name__ == '__main__':
    draw()
