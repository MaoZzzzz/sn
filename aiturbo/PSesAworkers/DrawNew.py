import numpy as np
import matplotlib.pyplot as plt

AITurbo2 = [1, 1, 1, 1, 1, 1]
AITurbo = [1.34, 1.24, 1.2, 1.17, 1.24, 1.24]
Centralized = [1.24, 1.47, 1.62, 2.65, 3.44, 3.92]
Optimus = [4.12, 3.94, 3.3, 2.63, 2.32, 1.98]
labels = ['2', '4', '6', '8', '10', '12']

fig, ax = plt.subplots(figsize=(4.1, 3))
# plt.rc('font', family="Times New Roman")

bar_width = 0.3
x = np.arange(len(labels)) * 2

ax.set_xticks(x)
ax.set_xticklabels(labels)

p1 = plt.bar(x - 3 * bar_width / 2, AITurbo2, color='brown', width=bar_width, align='center', edgecolor='black')
p2 = plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
p3 = plt.bar(x + bar_width / 2, Centralized, color='black', width=bar_width, align='center', edgecolor='black')
p4 = plt.bar(x + 3 * bar_width / 2, Optimus, color='grey', width=bar_width, align='center', edgecolor='black')

plt.ylabel('Norm. Avg. JCT', fontdict={'size': 16})
plt.xlabel('Average # of PSes/workers', fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.grid()

plt.tight_layout()
plt.subplots_adjust(bottom=0.23)
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('AITurbo-vGPU', 'AITurbo', 'Centralized', 'Optimus'), loc='upper left', fontsize=14)

plt.savefig('PSes_workers.eps')
plt.show()
