from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

jct = [1.64, 1.38, 1.0, 1.08, 1.27, 1.40]

labels = ['70', '60', '50', '40', '20', '10']
y = np.array(list(labels))

fig, ax = plt.subplots(figsize=(5, 5))
# plt.rc('font', family="Times New Roman")
bar_width = 0.78

plt.bar(range(len(jct)), jct, width=0.5, color='black', edgecolor='black', tick_label=labels)

plt.ylabel('Norm. Avg JCT', fontdict={'size': 25})
plt.xlabel('GPU ratio(%)', fontdict={'size': 25})
plt.tick_params(labelsize=20)

plt.ylim((0, 2.0))
ymajorLocator = MultipleLocator(0.5)
ax.yaxis.set_major_locator(ymajorLocator)

for a, b in zip(range(len(jct)), jct):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=17)
plt.subplots_adjust(left=0.2, bottom=0.3)
plt.savefig('gpu_percent.eps')
plt.show()