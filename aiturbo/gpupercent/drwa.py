import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    jct = [1.64, 1.38, 1.0, 1.08, 1.27, 1.40]
    # labels = ['VGG11', 'VGG16', 'VGG19', 'LeNet', 'GoogleNet', 'Overfeat', 'AlexNet', 'Trivial', 'Inception3',
    # 'Inception4', 'ResNet50', 'ResNet101', 'ResNet152', 'NasNet', 'MobileNet']
    labels = ['70', '60', '50', '40', '20', '10']
    y = np.array(list(labels))

    plt.bar(range(len(jct)), jct, width=0.5, color='black', linewidth=0.5, edgecolor='black', tick_label=labels)
    plt.xlabel("GPU ratio(%)")
    plt.ylabel("Norm. Avg JCT")
    # for a, b in zip(jct, y):
    #     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    for a, b in zip(range(len(jct)), jct):
        plt.text(a, b,
                 b,
                 ha='center',
                 va='bottom',
                 fontsize=7,
                 )
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.savefig('gpu_percent.jpg')
    plt.show()
