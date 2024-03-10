import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    # AITurbo = [1194.1, 2266]
    checkpoint = [1.3, 1.2, 1.8, 0.2, 0.5, 1.3, 0.9, 0.3, 2.1, 3.2, 1.4, 2.4, 4.1, 5.4, 1.5]
    labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'Overfeat', 'AlexNet', 'Trivial', 'Inception3',
              'Inception4', 'ResNet50', 'ResNet101', 'ResNet152', 'NasNet', 'MobileNet']

    total_width, n = 0.8, 6
    width = total_width / n

    plt.bar(range(len(checkpoint)), checkpoint, width=0.5, label='AITurbo2', color='black', linewidth=0.5,
            edgecolor='black', tick_label=labels)
    # plt.xlabel('Unpredictable(%):Predictable(%)')
    plt.ylabel('Checkpoint time (second)')
    plt.xticks(rotation=70, fontsize=5)
    plt.subplots_adjust(bottom=0.2)
    # plt.savefig('checkpointing.jpg')
    plt.show()
