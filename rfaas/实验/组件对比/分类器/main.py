import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimSun']

# knn, le, svr, mlp, rfr
rfaas = [97.62, 91.25, 92.91, 92.90, 99.70]
rfaas_wo_sc = [83.62, 79.07, 83.84, 83.90, 91.18]
rfaas_wo_dn = [92.43, 80.38, 88.43, 87.87, 93.24]
rfaas_wo_all = [73.62, 72.07, 72.03, 71.39, 80.84]

labels = ["KNN", "LR", "SVR", "MLP", "RFR"]

plt.figure(figsize=(6, 3))
bar_width = 0.3
opacity = 0.8

ind = np.array([1, 2.5, 4, 5.5, 7])
plt.bar(ind - bar_width - bar_width / 2, rfaas, bar_width, alpha=opacity, label='RFaaS', edgecolor='black')
plt.bar(ind - bar_width / 2, rfaas_wo_sc, bar_width, alpha=opacity, label='RFaaS-wo-sc', edgecolor='black')
plt.bar(ind + bar_width / 2, rfaas_wo_dn, bar_width, alpha=opacity, label='RFaaS-wo-dn', edgecolor='black')
plt.bar(ind + bar_width + bar_width / 2, rfaas_wo_all, bar_width, alpha=opacity, label='RFaaS-wo-scdn',
        edgecolor='black')

# plt.plot(ind, rfaas, marker='*', label='RFaas', linewidth=2)
# plt.plot(ind, rfaas_wo_sc, marker='o', label='KNN', linewidth=2)
# plt.plot(ind, rfaas_wo_dn, marker='.', label='RFR', linewidth=2)
# plt.plot(ind, rfaas_wo_all, marker='+', label='SVC', linewidth=2)

font = {'family': 'Times New Roman', 'size': 8}

for i, value in enumerate(rfaas):
    plt.text(ind[i] - bar_width - bar_width / 2, value, str(value), ha='center', va='bottom',
             fontdict=font)
for i, value in enumerate(rfaas_wo_sc):
    plt.text(ind[i] - bar_width / 2, value, str(value), ha='center', va='bottom',
             fontdict=font)
for i, value in enumerate(rfaas_wo_dn):
    plt.text(ind[i] + bar_width / 2, value, str(value), ha='center', va='bottom',
             fontdict=font)
for i, value in enumerate(rfaas_wo_all):
    plt.text(ind[i] + bar_width + bar_width / 2, value, str(value), ha='center', va='bottom',
             fontdict=font)

# for i in range(2):
#     plt.fill_between(ind, np.array(rfaas) + 0.5, np.array(rfaas) - 0.5, facecolor='blue', alpha=0.2)
#
#     plt.fill_between(ind, np.array(rfaas_wo_sc) + 0.5, np.array(rfaas_wo_sc) - 0.5, facecolor='orange', alpha=0.2)
#
#     plt.fill_between(ind, np.array(rfaas_wo_dn) + 0.5, np.array(rfaas_wo_dn) - 0.5, facecolor='green', alpha=0.2)
#
#     plt.fill_between(ind, np.array(rfaas_wo_all) + 0.5, np.array(rfaas_wo_all) - 0.5, facecolor='red', alpha=0.2)

plt.xticks(ind, labels, fontproperties='Times New Roman')
plt.tick_params(axis='both', which='major', labelsize=8, length=0)
plt.margins(x=0.05)
plt.ylim(0, 110)

plt.legend(loc='lower right', prop=font)
plt.ylabel('预测错误百分比', labelpad=5)
plt.xlabel('机器学习算法', labelpad=5)
plt.grid(True, linestyle='--')
plt.subplots_adjust(bottom=0.4)
plt.savefig("classifier_compare.pdf")
plt.show()
