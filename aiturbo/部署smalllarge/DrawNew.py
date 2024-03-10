import numpy as np
import matplotlib.pyplot as plt

AITurbo2 = [1, 1, 1, 1, 1]
AITurbo = [1.34, 1.24, 1.2, 1.17, 1.24]
Centralized = [1.24, 1.47, 2.12, 2.65, 3.44]
Optimus = [1.12, 1.94, 1.83, 1.73, 1.32]
labels = ['100:0', '75:25', '50:50', '25:75', '0:100']

fig, ax = plt.subplots(figsize=(4.1, 3))
# plt.rc('font', family="Times New Roman")

bar_width = 0.65
x = np.arange(len(labels)) * 3

ax.set_xticks(x)
ax.set_xticklabels(labels)

p1 = plt.bar(x - 3 * bar_width / 2, AITurbo2, color='brown', width=bar_width, align='center', edgecolor='black')
p2 = plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
p3 = plt.bar(x + bar_width / 2, Centralized, color='black', width=bar_width, align='center', edgecolor='black')
p4 = plt.bar(x + 3 * bar_width / 2, Optimus, color='grey', width=bar_width, align='center', edgecolor='black')

plt.ylabel('Norm. Avg. JCT', fontdict={'size': 16})
plt.xlabel('Small(%):Large(%)', fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.grid()

plt.tight_layout()
plt.subplots_adjust(bottom=0.23)
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('AITurbo-vGPU', 'AITurbo', 'Centralized', 'Optimus'), loc='upper left', fontsize=14)

plt.savefig('Smalllargejobs.eps')
plt.show()
