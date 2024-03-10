from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'Overfeat', 'AlexNet', 'Trivial', 'Inception3',
          'Inception4', 'ResNet50', 'ResNet101', 'ResNet152', 'NasNet', 'MobileNet']
data = [1.3, 1.2, 1.8, 0.2, 0.5, 1.3, 0.9, 0.3, 2.1, 3.2, 1.4, 2.4, 4.1, 5.4, 1.5]

fig, ax = plt.subplots(figsize=(5, 3.5))
# plt.rc('font', family="Times New Roman")

bar_width = 0.65
x = np.arange(len(labels))

ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.bar(x, data, color='black', width=bar_width, align='center')

# plt.xlabel('Model Name', fontdict={'size': 17})
plt.ylabel('Checkpoint time(second)', loc="top", fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.xticks(rotation=90)
plt.grid()

plt.ylim((0, 6))
ymajorLocator = MultipleLocator(1)
ax.yaxis.set_major_locator(ymajorLocator)

# plt.legend(loc="best", fontsize=20, framealpha=0.66, ncol=3)

plt.tight_layout()
plt.savefig('checkpointing.eps')
plt.show()
