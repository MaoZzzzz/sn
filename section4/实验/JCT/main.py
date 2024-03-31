from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
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

    plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, width=bar_width, align='center', edgecolor='black', label="Weaver")
    plt.bar(x - 3 * bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black', label="AITurbo")
    plt.bar(x - bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black', label="Optimus")
    plt.bar(x + bar_width / 2, Tiresias, width=bar_width, align='center', edgecolor='black', label="Tiresias")
    plt.bar(x + 3 * bar_width / 2, SRTF, width=bar_width, align='center', edgecolor='black', label="SRTF")
    plt.bar(x + 5 * bar_width / 2, FCFS, width=bar_width, align='center', edgecolor='black', label="FCFS",
            color="purple")

    # plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, width=bar_width, align='center', edgecolor='black', label="Weaver",
    #         color=(30 / 255, 70 / 255, 110 / 255))
    # plt.bar(x - 3 * bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black', label="AITurbo",
    #         color=(55 / 255, 103 / 255, 149 / 255))
    # plt.bar(x - bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black', label="Optimus",
    #         color=(82 / 255, 143 / 255, 173 / 255))
    # plt.bar(x + bar_width / 2, Tiresias, width=bar_width, align='center', edgecolor='black', label="Tiresias",
    #         color=(114 / 255, 188 / 255, 213 / 255))
    # plt.bar(x + 3 * bar_width / 2, SRTF, width=bar_width, align='center', edgecolor='black', label="SRTF",
    #         color=(170 / 255, 220 / 255, 224 / 255))
    # plt.bar(x + 5 * bar_width / 2, FCFS, width=bar_width, align='center', edgecolor='black', label="FCFS",
    #         color=(255 / 255, 230 / 255, 183 / 255))

    plt.xticks(x, labels)

    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)

    # plt.legend(fontsize=13, ncol=2, bbox_to_anchor=(0.75, 0.5))
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

    plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, width=bar_width, align='center', edgecolor='black',
            label='Weaver')
    plt.bar(x - 3 * bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black',
            label='AITurbo')
    plt.bar(x - bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black',
            label='Optimus')
    plt.bar(x + bar_width / 2, Tiresias, width=bar_width, align='center', edgecolor='black',
            label='Tiresias')
    plt.bar(x + 3 * bar_width / 2, SRTF, width=bar_width, align='center', edgecolor='black',
            label='SRTF')
    plt.bar(x + 5 * bar_width / 2, FCFS, width=bar_width, align='center', edgecolor='black',
            label='FCFS', color="purple")

    # plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, width=bar_width, align='center', edgecolor='black',
    #         label='Weaver', color=(30 / 255, 70 / 255, 110 / 255))
    # plt.bar(x - 3 * bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black',
    #         label='AITurbo', color=(55 / 255, 103 / 255, 149 / 255))
    # plt.bar(x - bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black',
    #         label='Optimus', color=(82 / 255, 143 / 255, 173 / 255))
    # plt.bar(x + bar_width / 2, Tiresias, width=bar_width, align='center', edgecolor='black',
    #         label='Tiresias', color=(114 / 255, 188 / 255, 213 / 255))
    # plt.bar(x + 3 * bar_width / 2, SRTF, width=bar_width, align='center', edgecolor='black',
    #         label='SRTF', color=(170 / 255, 220 / 255, 224 / 255))
    # plt.bar(x + 5 * bar_width / 2, FCFS, width=bar_width, align='center', edgecolor='black',
    #         label='FCFS', color=(255 / 255, 230 / 255, 183 / 255))

    plt.xticks(x, labels)

    plt.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)

    # plt.legend(fontsize=13, ncol=2, loc='upper right')
    plt.ylabel('归一化时间', labelpad=5, fontsize=13)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.savefig("long_short_jct.pdf")
    plt.show()


def legend():
    AITurbo_vGPU = [1, 1]
    AITurbo = [1.24, 1.14]
    Optimus = [4.1, 2.9]
    Tiresias = [3.1, 3.9]
    SRTF = [2.1, 3.6]
    FCFS = [8, 3.9]
    labels = ['Short Job', 'Long Job']

    fig, ax = plt.subplots(figsize=(10, 2))

    # plt.rc('font', family="Times New Roman")

    bar_width = 0.3
    x = np.arange(len(labels)) * 2

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    p1 = plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, width=bar_width, align='center', edgecolor='black',
                 label='Weaver')
    p2 = plt.bar(x - 3 * bar_width / 2, AITurbo, width=bar_width, align='center', edgecolor='black',
                 label='AITurbo')
    p3 = plt.bar(x - bar_width / 2, Optimus, width=bar_width, align='center', edgecolor='black',
                 label='Optimus')
    p4 = plt.bar(x + bar_width / 2, Tiresias, width=bar_width, align='center', edgecolor='black',
                 label='Tiresias')
    p5 = plt.bar(x + 3 * bar_width / 2, SRTF, width=bar_width, align='center', edgecolor='black',
                 label='SRTF')
    p6 = plt.bar(x + 5 * bar_width / 2, FCFS, width=bar_width, align='center', edgecolor='black',
                 label='FCFS', color="purple")

    plt.cla()
    plt.clf()
    plt.axis('off')

    # plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('AITurbo-vGPU', 'AITurbo', 'Optimus', 'Tiresias', 'SRTF', 'FCFS'),
    #            loc='upper left', bbox_to_anchor=(-0.21, 1.9), ncol=6, fontsize=20)

    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]),
               ('Weaver', 'AITurbo', 'Optimus', 'Tiresias', 'SRTF', 'FCFS'),
               bbox_to_anchor=(-0.1, 0.9), loc='upper left', ncol=3, fontsize=18)

    plt.tight_layout()
    plt.savefig('legend-all.pdf', bbox_inches='tight')
    plt.show()


def train_queue_jct():
    queueing_time = [9, 30, 57, 80, 50, 145]
    training_time = [85, 80, 98, 180, 170, 175]

    labels = ['Weaver', 'AIT.', 'Opt.', 'Tire.', 'SRTF', 'FCFS']

    plt.figure(figsize=(5, 3))
    bar_width = 0.6
    x = np.arange(len(labels))

    p1 = plt.bar(labels, training_time, width=bar_width, edgecolor='black', align='center')
    p2 = plt.bar(labels, queueing_time, width=bar_width, bottom=np.array(training_time), align='center',
                 edgecolor='black')

    plt.xticks(x, labels)

    plt.ylabel('时间（分钟）', fontdict={'size': 13})
    plt.tick_params(labelsize=13)
    plt.grid()

    plt.legend((p1[0], p2[0]), ('平均训练时间', '平均排队时间'), loc='upper left', fontsize=13)

    # plt.tight_layout()
    # plt.xticks(rotation=30)
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.savefig('train_queue_jct.pdf')
    plt.show()


def new_old():
    AITurbo_vGPU = [1, 1, 1]
    # AITurbo = [1.24, 1.26, 1.3]
    Optimus = [2.2, 2.6, 2.65]
    Tiresias = [3.8, 3.6, 3.5]

    labels = ['25:75', '50:50', '75:25']

    fig, ax = plt.subplots(figsize=(5, 3))
    # plt.rc('font', family="Times New Roman")

    bar_width = 0.3
    x = np.arange(len(labels)) * 2

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    p1 = plt.bar(x - bar_width, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
    # plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
    p2 = plt.bar(x, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
    p3 = plt.bar(x + bar_width, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')

    plt.ylabel('Norm. Avg. JCT', fontdict={'size': 16})
    plt.xlabel('New jobs(%):Old jobs(%)', fontdict={'size': 16})
    plt.tick_params(labelsize=14)
    plt.grid()

    ax.set_ylim([0, 6])
    ymajorLocator = MultipleLocator(2)
    ax.yaxis.set_major_locator(ymajorLocator)

    y = [0.99, 0.95, 0.91]
    ax2 = plt.twinx()

    plt.ylabel('Accuracy', fontdict={'size': 16})
    # plt.yticks(fontproperties='Times New Roman')
    plt.tick_params(labelsize=16)

    ax2.set_ylim([0.5, 1.0])
    ymajorLocator = MultipleLocator(0.25)
    ax2.yaxis.set_major_locator(ymajorLocator)

    plt.plot(x, y, "r", marker='.', c='r', ms=5, linewidth='1')

    plt.legend((p1[0], p2[0], p3[0]), ('Weaver', 'Optimus', 'Tiresias'), loc='upper left')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.23)
    # plt.savefig('new_job_percent.eps')
    plt.show()


if __name__ == '__main__':
    # train_queue_jct()
    new_old()