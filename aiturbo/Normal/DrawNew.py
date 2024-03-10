from matplotlib import pyplot as plt
import numpy as np

AITurbo_vGPU = [1, 1]
AITurbo = [1.24, 1.34]
Optimus = [1.8, 2.1]
Tiresias = [2.8, 3.394]
SRTF = [1.9, 4.694]
FCFS = [4.2, 3.394]

labels = ['JCT', 'makespan']

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
plt.grid()

plt.tight_layout()
# plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('AITurbo-vGPU', 'AITurbo', 'Optimus', 'Tiresias', 'SRTF', 'FCFS'), loc="upper left", ncol=2,
#            fontsize=20, framealpha=0.5)
plt.savefig('overall_comparison.eps')
plt.show()
