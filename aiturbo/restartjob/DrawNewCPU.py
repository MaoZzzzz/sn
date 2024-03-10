import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'Overfeat', 'AlexNet', 'Trivial', 'Inception3',
          'Inception4', 'ResNet50', 'ResNet101', 'ResNet152', 'NasNet', 'MobileNet']
warm_up = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
load_checkpoint = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 0]
build_model = [220, 340, 490, 30, 100, 399, 80, 10, 380, 400, 410, 520, 610, 110, 50]

all = [490, 710, 890, 30, 210, 900, 170, 10, 630, 830, 820, 1090, 1240, 360, 90]

for i in range(len(warm_up)):
    warm_up[i] = all[i] - build_model[i] - load_checkpoint[i]


fig, ax = plt.subplots(figsize=(5, 3.5))
# plt.rc('font', family="Times New Roman")

width = 0.65
x = np.arange(len(labels))

ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.bar(labels, build_model, width, label='build model', color='black', linewidth=1.0, edgecolor='black')
plt.bar(labels, load_checkpoint, width, bottom=np.array(build_model), label='load checkpoint', color='red',
        linewidth=1.0, edgecolor='black')
plt.bar(labels, warm_up, width, bottom=np.array(build_model) + np.array(load_checkpoint), label='warm up',
        color='grey', linewidth=1.0, edgecolor='black')

plt.ylabel('Time (second)', fontdict={'size': 16})
plt.tick_params(labelsize=14)
plt.xticks(rotation=90)
plt.grid()

ax.set_ylim([0, 1200])
ymajorLocator = MultipleLocator(200)
ax.yaxis.set_major_locator(ymajorLocator)

plt.legend(loc="upper left", fontsize=14)

plt.tight_layout()
plt.savefig('checkpoint_load_time_cpu.eps')
plt.show()