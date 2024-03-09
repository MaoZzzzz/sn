import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

# fcfs. srtf, sdf, rfaas
fcfs = [1.0, 0.631, 0.128]
sdf = [1.0, 0.715, 0.289]
srtf = [1.0, 0.824, 0.436]
rfaas = [1.0, 0.965, 0.712]

labels = ["稀疏型", "阶段型", "突发型"]

plt.figure(figsize=(6, 3))
bar_width = 0.2
opacity = 0.8

ind = np.array([1, 2, 3])
plt.bar(ind - bar_width - bar_width / 2, fcfs, bar_width, alpha=opacity, label='OpenFaas$_{FCFS}^+$', edgecolor='black')
plt.bar(ind - bar_width / 2, sdf, bar_width, alpha=opacity, label='OpenFaas$_{SDF}^+$', edgecolor='black')
plt.bar(ind + bar_width / 2, srtf, bar_width, alpha=opacity, label='OpenFaas$_{SRTF}^+$', edgecolor='black')
plt.bar(ind + bar_width + bar_width / 2, rfaas, bar_width, alpha=opacity, label='RFaas', edgecolor='black')

plt.xticks(ind, labels)
plt.tick_params(axis='both', which='major', labelsize=10, length=0)
# plt.margins(x=0.05)

plt.legend(fontsize=10, loc='lower left')
plt.ylabel('调度成功率', labelpad=5)
plt.xlabel('负载类型', labelpad=5)
plt.grid(True, linestyle='--')
plt.subplots_adjust(bottom=0.2)
plt.savefig("scheduler_compare.pdf")
plt.show()
