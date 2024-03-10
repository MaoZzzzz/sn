from matplotlib import pyplot as plt
import numpy as np

AITurbo_vGPU = [1, 1]
AITurbo = [1.24, 1.14]
Optimus = [4.1, 2.9]
Tiresias = [3.1, 3.9]
SRTF = [2.1, 3.6]
FCFS = [8, 3.9]

labels = ['Short Job', 'Long Job']

fig, ax = plt.subplots(figsize=(5, 3.5))

# plt.rc('font', family="Times New Roman")

bar_width = 0.3
x = np.arange(len(labels)) * 2

ax.set_xticks(x)
ax.set_xticklabels(labels)

p1 = plt.bar(x - 5 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
p2 = plt.bar(x - 3 * bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
p3 = plt.bar(x - bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
p4 = plt.bar(x + bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')
p5 = plt.bar(x + 3 * bar_width / 2, SRTF, color='lightgrey', width=bar_width, align='center', edgecolor='black')
p6 = plt.bar(x + 5 * bar_width / 2, FCFS, color='white', width=bar_width, align='center', edgecolor='black')

plt.ylabel('Norm. Avg. JCT', fontdict={'size': 20})
plt.tick_params(labelsize=20)

# plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('AITurbo-vGPU', 'AITurbo', 'Optimus', 'Tiresias', 'SRTF', 'FCFS'),
#            loc='upper left', bbox_to_anchor=(-1.0, 1.2), ncol=6, fontsize=18)

plt.grid()

plt.tight_layout()
plt.savefig('long_short.eps')
plt.show()
