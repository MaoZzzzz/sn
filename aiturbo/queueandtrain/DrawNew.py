from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

queueing_time = [9, 24, 57, 80, 50, 145]
training_time = [85, 80, 98, 180, 170, 175]

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

# labels = ['AIT.1', 'AIT.2', 'AIT.', 'AIT.4', 'AIT.5', 'AIT.6']
labels = ['AI-vGPU', 'AITurbo', 'Optimus', 'Tiresias', 'SRTF', 'FCFS']

fig, ax = plt.subplots(figsize=(4.1, 3))
# plt.rc('font', family="Arial")

bar_width = 0.6
x = np.arange(len(labels))

ax.set_xticks(x)
ax.set_xticklabels(labels)

p1 = plt.bar(labels, training_time, width=bar_width, color='black', edgecolor='black', align='center')
p2 = plt.bar(labels, queueing_time, width=bar_width, bottom=np.array(training_time), color='red', align='center',
        edgecolor='black')

plt.ylabel('Time (min)', fontdict={'size': 16})
# plt.xlabel('New jobs(%):Old jobs(%)', fontdict={'size': 20})
plt.tick_params(labelsize=14)
plt.grid()

ax.set_ylim([0, 400])
ymajorLocator = MultipleLocator(100)
ax.yaxis.set_major_locator(ymajorLocator)

# plt.legend((p1[0], p2[0]), ('Avg.Training time', 'Avg.Training time'), bbox_to_anchor=(-0.1, 0.9), loc='upper left', ncol=6, fontsize=20)
plt.legend((p1[0], p2[0]), ('Avg.Training time', 'Avg.Queueing time'), loc='upper left', fontsize=14)

plt.tight_layout()
plt.xticks(rotation=30)
plt.subplots_adjust(bottom=0.23)
# plt.savefig('trainqueue.eps')
plt.show()
