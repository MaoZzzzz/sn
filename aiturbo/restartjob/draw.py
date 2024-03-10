import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(['ieee', 'grid']):
    labels = ['VGG11-1-GPU', 'VGG11-2-GPU', 'VGG11-3-GPU', 'VGG16-1-GPU', 'VGG16-2-GPU', 'VGG16-3-GPU', 'VGG19-1-GPU',
              'VGG19-2-GPU', 'VGG19-3-GPU', 'LeNet-1-GPU', 'LeNet-2-GPU', 'LeNet-3-GPU', 'Google.-1-GPU',
              'Google.-2-GPU', 'Google.-3-GPU', 'Overfeat-1-GPU', 'Overfeat-2-GPU', 'Overfeat-3-GPU', 'AlexNet-1-GPU',
              'AlexNet-2-GPU', 'AlexNet-3-GPU', 'Trivial-1-GPU', 'Trivial-2-GPU', 'Trivial-3-GPU', 'Incep.3-1-GPU',
              'Incep.3-2-GPU', 'Incep.3-3-GPU', 'Incep.4-1-GPU', 'Incep.4-2-GPU', 'Incep.4-3-GPU', 'Res.50-1-GPU',
              'Res.50-2-GPU', 'Res.50-3-GPU', 'Res.101-1-GPU', 'Res.101-2-GPU', 'Res.101-3-GPU', 'Res.152-1-GPU',
              'Res.152-2-GPU', 'Res.152-3-GPU', 'NasNet-1-GPU', 'NasNet-2-GPU', 'NasNet-3-GPU', 'MobileNet-1-GPU',
              'MobileNet-2-GPU', 'MobileNet-3-GPU']
    warm_up = [9.342, 19.453, 22.345, 10.23, 19.453, 22.345, 10.98, 19.453, 22.345, 0.23, 0.34, 0.23, 1.345, 1.564,
               1.234, 5.47, 17.347, 19.043, 4.571, 6.124, 7.435, 0.4, 0.54, 0.53, 4.563, 5.325, 5.342, 6.012, 6.142,
               6.213, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 0.23,
               0.34, 0.23]
    load_checkpoint = [1.431, 1.523, 2.133, 1.431, 1.535, 2.136, 1.433, 1.531, 2.132, 0.233, 0.341, 0.235, 0.238, 0.346,
                       0.273, 2.471,
                       2.465, 3.213, 0.238, 0.346, 0.273, 0.238, 0.346, 0.273, 3.261, 3.743, 4.023,
                       5.012, 5.142, 5.213, 1.343, 1.534, 1.752, 4.633, 4.693, 4.833, 6.432, 6.534, 6.987, 7.563, 7.985,
                       8.023, 0.98, 1.34, 1.56]
    build_model = [9.342, 19.453, 22.345, 10.23, 19.453, 22.345, 10.98, 19.453, 22.345, 0.23, 0.34, 0.23, 1.345, 1.564,
                   1.234, 5.47, 17.347, 19.043, 4.571, 6.124, 7.435, 0.4, 0.54, 0.53, 4.563, 5.325, 5.342, 6.012, 6.142,
                   6.213, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 4.563, 5.325, 5.342, 0.23,
                   0.34, 0.23]

    all = [25, 42, 58, 27, 43, 60, 30, 46, 61, 6, 11, 17, 11, 19, 21, 20, 44, 53, 11, 22, 27, 4, 7, 9, 22, 38, 43, 39,
           43, 46, 21, 29, 36, 35, 42, 54, 41, 54, 63, 61, 79, 94, 10, 21, 24]
    for i in range(len(warm_up)):
        warm_up[i] = all[i] - build_model[i] - load_checkpoint[i]
    width = 0.5

    # plt.figure(figsize=(9, 5))
    # plt.bar(labels, build_model, width, label='build model', color='black', linewidth=1.0, edgecolor='black')
    # plt.bar(labels, load_checkpoint, width, bottom=np.array(build_model), label='load checkpoint', color='red',
    #         linewidth=1.0, edgecolor='black')
    # plt.bar(labels, warm_up, width, bottom=np.array(build_model) + np.array(load_checkpoint), label='warm up',
    #         color='grey', linewidth=1.0, edgecolor='black')
    # # plt.xlabel('Unpredictable(%):Predictable(%)')
    # plt.xticks(rotation=90, size=7, weight='bold')
    # plt.ylabel('Time (second)')
    # plt.subplots_adjust(left=0.1, bottom=0.2)
    # plt.legend(loc='best')
    # plt.savefig('checkpoint_load_time.jpg')
    # plt.show()

    fig, ax = plt.subplots(figsize=(18, 7.2))
    plt.rc('font', family="Times New Roman")
    bar_width = 0.78

    lx = np.arange(len(labels)) * 1
    x = np.arange(len(labels)) * 1

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    plt.bar(labels, build_model, width, label='build model', color='black', linewidth=1.0, edgecolor='black')
    plt.bar(labels, load_checkpoint, width, bottom=np.array(build_model), label='load checkpoint', color='red',
            linewidth=1.0, edgecolor='black')
    plt.bar(labels, warm_up, width, bottom=np.array(build_model) + np.array(load_checkpoint), label='warm up',
            color='grey', linewidth=1.0, edgecolor='black')

    plt.ylabel('Time (second)', fontdict={'family': 'Times New Roman', 'size': 35})

    plt.tick_params(labelsize=28)
    plt.xticks(rotation=90)
    plt.grid()
    plt.legend(loc='best', fontsize=25, framealpha=0.66, ncol=3)
    plt.tight_layout()
    plt.margins(x=0.008)

    plt.savefig('checkpoint_load_time.pdf')
    plt.show()
