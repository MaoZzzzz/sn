from matplotlib import pyplot as plt
import numpy as np

AITurbo_vGPU = [1, 1, 1, 1, 1]
AITurbo = [1.48, 1.34, 1.24, 1.1, 1]
Optimus = [2.1, 2.2, 2.5, 3.3, 3.9]
Tiresias = [5.3, 4.3, 3.9, 3.3, 2.2]

labels = ['0:100', '25:75', '50:50', '75:25', '100:0']


def histogram():
    fig, ax = plt.subplots()

    plt.rc('font', family="Times New Roman")

    bar_width = 0.78
    x = np.arange(len(labels)) * 5

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    plt.bar(x - 3 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
    plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
    plt.bar(x + 3 * bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')

    plt.ylabel('Norm. Avg. JCT', fontdict={'family': 'Times New Roman', 'size': 35})
    plt.xlabel('Unpredictable(%):Predictable(%)', fontdict={'family': 'Times New Roman', 'size': 35})

    plt.tick_params(labelsize=28)

    plt.tight_layout()
    plt.margins(x=0.008)

    # plt.savefig('predict_job_percent.pdf')
    plt.show()


def line_chart():
    y = [0.95, 0.97, 0.98, 0.94, 0.95]

    fig, ax = plt.subplots()

    plt.ylabel('Accuracy', fontdict={'family': 'Times New Roman', 'size': 35})
    ax.set_ylim([0.5, 1.0])

    plt.tick_params(labelsize=28)
    plt.xticks(size=25)
    plt.plot(labels, y, marker='D', color='red', linewidth=1.8, markersize=8, linestyle='-')
    plt.rc('font', family="Times New Roman")
    plt.tight_layout()
    plt.savefig('predict_line_chart.pdf')
    plt.show()


def draw_legend():
    y = [0.95, 0.97, 0.98, 0.94, 0.95]
    # p1 = plt.plot(AITurbo_vGPU, y, marker='D', color='red', linewidth=1.8, markersize=8, linestyle='-')
    # p2 = plt.plot(AITurbo, y, marker='D', color='red', linewidth=1.8, markersize=8, linestyle='-')
    # p3 = plt.plot(Optimus, y, marker='D', color='red', linewidth=1.8, markersize=8, linestyle='-')
    # p4 = plt.plot(Tiresias, y, marker='D', color='red', linewidth=1.8, markersize=8, linestyle='-')
    p1 = plt.bar()
    p2 = plt.bar()
    p3 = plt.bar()
    p4 = plt.bar()
    plt.legend((p1[0], p2[0], p3[0], p4[0],), ('AITurbo-vGPU', 'AITurbo', 'Optimus', 'Tiresias'), loc="upper left", fontsize=20,
               framealpha=0.5)
    plt.show()


if __name__ == '__main__':
    histogram()
    # line_chart()
    # draw_legend()