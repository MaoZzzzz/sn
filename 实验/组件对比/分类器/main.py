import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

# knn, le, svr, mlp, rfr
rfaas = [97.62, 91.25, 92.91, 92.90, 99.70]
rfaas_wo_sc = [83.62, 79.07, 83.84, 83.90, 91.18]

labels = ["KNN", "LR", "SVR", "MLP", "RFR"]

plt.figure(figsize=(4, 2))
bar_width = 0.4
opacity = 0.8

ind = np.arange(len(labels))
plt.bar(ind - bar_width / 2, rfaas, bar_width, alpha=opacity, label='RFaas', edgecolor='black')
plt.bar(ind + bar_width / 2, rfaas_wo_sc, bar_width, alpha=opacity, label='RFaas-', edgecolor='black')

for i, value in enumerate(rfaas):
    plt.text(ind[i] - bar_width / 2, value, str(value), ha='center', va='bottom', fontsize=8)
for i, value in enumerate(rfaas_wo_sc):
    plt.text(ind[i] + bar_width / 2, value, str(value), ha='center', va='bottom', fontsize=8)

plt.xticks(ind, labels)
plt.tick_params(axis='both', which='major', labelsize=8, length=0)
plt.margins(x=0.05)
plt.ylim(20, 110)

plt.legend(fontsize=8, loc='lower right')
plt.ylabel('预测错误百分比', labelpad=5)
plt.xlabel('函数名称', labelpad=5)
plt.grid(True, linestyle='--')
plt.subplots_adjust(bottom=0.2)
plt.savefig("classifier_compare.pdf")
plt.show()
