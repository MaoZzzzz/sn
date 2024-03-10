import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    labels = ['AIT.-vGPU', 'AIT.', 'Optim.', 'Tires.', 'SRTF', 'FCFS']
    queueing_time = [9, 24, 57, 80, 50, 145]
    training_time = [85, 80, 98, 180, 170, 175]
    trai_time = [85, 80, 98, 180, 170, 175]

    width = 0.7

    plt.gca().spines['bottom'].set_linewidth(1.0)
    plt.gca().spines['left'].set_linewidth(1.0)
    plt.gca().spines['top'].set_linewidth(1.0)
    plt.gca().spines['right'].set_linewidth(1.0)
    plt.bar(labels, training_time, width, label='Avg.Queueing time', color='black', linewidth=1.0, edgecolor='black')
    plt.bar(labels, queueing_time, width, bottom=np.array(training_time), label='Avg.Training time', color='red', linewidth=1.0,
            edgecolor='black')
    plt.bar(labels, trai_time, width, bottom=np.array(training_time)+np.array(queueing_time), label='Avg', color='grey', linewidth=1.0,
            edgecolor='black')

    plt.ylabel('Time (min)', fontsize=12)
    plt.yticks(size=8)
    plt.xticks(size=8)
    plt.legend(loc='best')
    plt.subplots_adjust(left=0.2)

    # plt.savefig('queue_train.jpg')
    plt.show()
