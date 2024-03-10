import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# with plt.style.context(['ieee', 'grid']):
#     data = [0.23, 0.29, 0.30, 0.01, 0.05, 0.06, 0.28, 0.48, 0.25, 0.36, 0.52, 0.17, 0.16, 0.01, 0.05]
#     for i in range(len(data)):
#         data[i] = data[i] * 11
#     labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'AlexNet', 'Inception3', 'Inception4', 'Resnet50',
#               'Resnet101', 'Resnet152', 'NasNet', 'Overfeat', 'Trivial', 'MobileNet']
#
#     total_width, n = 1.2, 4
#     width = total_width / n
#
#     # plt.figure(figsize=(8, 4))
#
#     plt.barh(range(len(data)), data, color='black', linewidth=0.4, edgecolor='black', tick_label=labels)
#     plt.ylabel('Memory Usage (GB)', fontdict={'family': 'Times New Roman'})
#     plt.xticks(fontproperties='Times New Roman', size=15)
#     plt.yticks(fontproperties='Times New Roman', size=11)
#     plt.subplots_adjust(left=0.25, bottom=0.2)
#     plt.legend(loc='best')
#     plt.savefig('memory_usage.pdf')
#     plt.show()


data = [0.23, 0.29, 0.30, 0.01, 0.05, 0.06, 0.28, 0.48, 0.25, 0.36, 0.52, 0.17, 0.16, 0.01, 0.05]
for i in range(len(data)):
    data[i] = data[i] * 11
labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'AlexNet', 'Inception3', 'Inception4', 'Resnet50',
          'Resnet101', 'Resnet152', 'NasNet', 'Overfeat', 'Trivial', 'MobileNet']

fig, ax = plt.subplots()
plt.rc('font', family="Times New Roman")

plt.barh(range(len(data)), data, height=0.8, color='black', edgecolor='black', tick_label=labels)

plt.grid(ls='-.', lw=0.25)
plt.ylabel('Memory Usage (GB)', fontdict={'family': 'Times New Roman', 'size': 25})
plt.xticks(fontproperties='Times New Roman', size=25)
plt.yticks(fontproperties='Times New Roman', size=25)

plt.subplots_adjust(left=0.33)
plt.legend(loc='best')
plt.savefig('memory_usage.pdf')
plt.show()
