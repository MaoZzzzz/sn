from matplotlib import pyplot as plt
import numpy as np

AITurbo_vGPU = [1, 1, 1]
AITurbo = [1.24, 1.1, 1.24]
Optimus = [2.2, 2.9, 2.3]
Tiresias = [3.8, 4.1, 3.9]

labels = ['100:0', '0:100', '50:50']

fig, ax = plt.subplots(figsize=(11.0, 0.5))

# plt.rc('font', family="Times New Roman")

bar_width = 0.78
lx = np.arange(len(labels)) * 3
x = np.arange(len(labels)) * 5

ax.set_xticks(x)
ax.set_xticklabels(labels)

p1 = plt.bar(x - 3 * bar_width / 2, AITurbo_vGPU, color='brown', width=bar_width, align='center', edgecolor='black')
p2 = plt.bar(x - bar_width / 2, AITurbo, color='red', width=bar_width, align='center', edgecolor='black')
p3 = plt.bar(x + bar_width / 2, Optimus, color='black', width=bar_width, align='center', edgecolor='black')
p4 = plt.bar(x + 3 * bar_width / 2, Tiresias, color='grey', width=bar_width, align='center', edgecolor='black')

plt.cla()
plt.clf()
plt.axis('off')

plt.legend((p1[0], p2[0], p3[0], p4[0]), ('AITurbo-vGPU', 'AITurbo', 'Optimus', 'Tiresias'), bbox_to_anchor=(-0.1, 0.9),
           loc='upper left', ncol=6, fontsize=20)

plt.tight_layout()
plt.savefig('legend.eps', bbox_inches='tight')
plt.show()

