from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

jct = [0.014, 0.101, 0.382, 0.701, 1.097, 1.419]

labels = ['20', '100', '300', '500', '700', '1000']
y = np.array(list(labels))

fig, ax = plt.subplots(figsize=(5, 5))
# plt.rc('font', family="Times New Roman")
bar_width = 0.78

plt.bar(range(len(jct)), jct, width=0.5, color='black', edgecolor='black', tick_label=labels)

plt.ylabel('Time(second)', fontdict={'size': 25})
plt.xlabel('Number of jobs', fontdict={'size': 25})
plt.tick_params(labelsize=20)
# plt.xticks(rotation=70)

plt.ylim((0, 2.0))
ymajorLocator = MultipleLocator(0.5)
ax.yaxis.set_major_locator(ymajorLocator)

for a, b in zip(range(len(jct)), jct):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=17)
plt.subplots_adjust(left=0.2, bottom=0.3)
plt.savefig('ttp_overhead.eps')
plt.show()