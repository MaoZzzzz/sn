import  matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

def memory_usage():
    labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'AlexNet', 'Inception3', 'Inception4', 'Resnet50',
              'Resnet101', 'Resnet152', 'NasNet', 'Overfeat', 'Trivial', 'MobileNet']
    data = [0.23, 0.29, 0.30, 0.01, 0.05, 0.06, 0.28, 0.48, 0.25, 0.36, 0.52, 0.17, 0.16, 0.01, 0.05]
    for i in range(len(data)):
        data[i] = data[i] * 11

    fig, ax = plt.subplots()
    bar_width = 0.78
    x = np.arange(len(labels))
    # plt.rc('font', family="Times New Roman")
    plt.barh(x, data, color='black', height=bar_width, align='center', tick_label=labels)
    plt.ylabel('Model Name', fontdict={'size': 25})
    plt.xlabel('Memory Usage (GB)', fontdict={'size': 25})
    plt.tick_params(labelsize=20)
    plt.grid()

    plt.xlim((0, 6))
    x_major_locator = MultipleLocator(2)
    ax.xaxis.set_major_locator(x_major_locator)

    plt.tight_layout()
    plt.margins(x=0.008)
    plt.savefig('memory_usage.eps')
    plt.show()


def sm_jct():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    y = [1.0, 0.8463852434490531, 0.44971728860380655, 0.48769320846031045, 0.45268981515826007, 0.31287472633176205,
         0.3719970812203452, 0.34585277509168705, 0.2935250096768853, 0.2739675330197389, 0.18584462621380843,
         0.1701389990537554, 0.21392728872863875, 0.1666123807609167, 0.16953553663425755, 0.2187562329635606,
         0.19807045381565466, 0.13222625597298446, 0.17691849705392707, 0.18629911081816763, 0.17358280445924423,
         0.16208945720123738, 0.1621749554860889, 0.11229996296379817, 0.1387181811864256, 0.14730910815978135,
         0.14645687887281092, 0.10580402027707987, 0.04840461058052032, 0.10511352234090018, 0.08226022130501445,
         0.10447213526576887, 0.02278695131273676, 0.08858255881973509, 0.07041998150676439, 0.09030840695876513,
         -0.03960325812546092, 0.023591015625333698, 0.07625012288476554, 0.04525136235151361, 0.05040627542295247,
         0.06660100920685995, 0.1010968668080425, 0.036425919442041536, 0.007574364151335978, 0.058271482021692515,
         0.059086343252233435, 0.07587293895451518, 0.04095961690323749, 0.10113529339885778]
    yvals = [1.00204405, 0.75170439, 0.60139469, 0.50114405, 0.4295148, 0.37578102,
             0.33398107, 0.30053668, 0.27317016, 0.25036272, 0.23106269, 0.21451876,
             0.20017991, 0.18763283, 0.17656141, 0.16671979, 0.15791384, 0.14998825,
             0.14281729, 0.13629808, 0.13034563, 0.1248891, 0.119869, 0.11523499,
             0.11094417, 0.10695978, 0.10325012, 0.09978773, 0.09654869, 0.09351205,
             0.09065942, 0.08797456, 0.0854431, 0.08305226, 0.08079063, 0.07864803,
             0.07661528, 0.07468415, 0.07284722, 0.07109775, 0.06942964, 0.06783734,
             0.0663158, 0.06486041, 0.06346695, 0.06213153, 0.06085062, 0.05962094,
             0.05843948, 0.05730346]

    fig, ax = plt.subplots()
    plt.scatter(x, y, s=50)

    # plt.rc('font', family="Times New Roman")
    plt.ylabel('Norm. Avg. JCT', fontdict={'size': 25})
    plt.xlabel('Resource Proportion(%)', fontdict={'size': 25})
    plt.tick_params(labelsize=20)

    plt.plot(x, yvals, color='g', markersize=10, linewidth=3)
    plt.grid()

    plt.tight_layout()
    plt.savefig('sm_jct.eps')
    plt.show()


if __name__ == '__main__':
    memory_usage()
    # sm_jct()