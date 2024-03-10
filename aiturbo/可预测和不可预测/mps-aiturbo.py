import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

AITurbo2 = [1, 1, 1, 1, 1]
AITurbo = [1.48, 1.34, 1.24, 1.1, 1]
Optimus = [2.1, 2.2, 2.5, 3.3, 3.9]
Tiresias = [5.3, 4.3, 3.9, 3.3, 2.2]
labels = ['0:100', '25:75', '50:50', '75:25', '100:0']

fig, ax = plt.subplots(figsize=(5, 3))
# plt.rc('font', family="Times New Roman")

bar_width = 0.3
x = np.arange(len(labels)) * 2

ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.bar(x - 3 * bar_width / 2, AITurbo2, color='brown', width=bar_width, align='center', edgecolor='black')
plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
plt.bar(x + bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
plt.bar(x + 3 * bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')

plt.xlabel('Unpredictable(%):Predictable(%)', fontdict={'size': 16})
plt.ylabel('Norm. Avg. JCT', fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.grid()

ax.set_ylim([0, 6])
ymajorLocator = MultipleLocator(2)
ax.yaxis.set_major_locator(ymajorLocator)

y = [0.95, 0.97, 0.98, 0.94, 0.95]
ax2 = plt.twinx()

plt.ylabel('Accuracy', fontdict={'size': 16})
plt.tick_params(labelsize=16)

ax2.set_ylim([0.5, 1.0])
ymajorLocator = MultipleLocator(0.25)
ax2.yaxis.set_major_locator(ymajorLocator)

plt.plot(x, y, "r", marker='.', c='r', ms=5, linewidth='1')

plt.tight_layout()
plt.subplots_adjust(bottom=0.23)
plt.savefig('predictable.eps', dpi=100)
plt.show()
