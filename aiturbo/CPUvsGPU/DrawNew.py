from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

AITurbo_vGPU = [1, 1]
AITurbo = [1.34, 1.14]
Optimus = [2.4, 3.1]
Tiresias = [3.4, 4.9]

labels = ['100:0', '75:25']

fig, ax = plt.subplots(figsize=(5, 3))
# plt.rc('font', family="Times New Roman")

bar_width = 0.3
x = np.arange(len(labels)) * 2

ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.bar(x - 3 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
plt.bar(x + bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
plt.bar(x + 3 * bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')

plt.xlabel('GPU jobs(%):CPU jobs(%)', fontdict={'size': 16})
plt.ylabel('Norm. Avg. JCT', fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.grid()

y = [0.97, 0.98]
ax2 = plt.twinx()

plt.ylabel('Accuracy', fontdict={'size': 16})
# plt.yticks(fontproperties='Times New Roman')
plt.tick_params(labelsize=16)

ax2.set_ylim([0.5, 1.0])
ymajorLocator = MultipleLocator(0.25)
ax2.yaxis.set_major_locator(ymajorLocator)

plt.plot(x, y, "r", marker='.', c='r', ms=5, linewidth='1')

plt.tight_layout()
plt.subplots_adjust(bottom=0.23)
plt.savefig('gpu_job_percent.eps')
plt.show()
