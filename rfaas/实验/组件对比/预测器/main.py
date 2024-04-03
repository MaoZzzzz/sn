import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

plt.rcParams['font.sans-serif'] = ['Times New Roman']


def box_float():
    float = [[1.3, 3.2, 5.6, 6.1, 9.7], [1, 2.4, 4, 5.2, 8.5], [1.7, 3.4, 6.8, 9, 13.5], [2, 5.2, 8, 12, 17],
             [2.1, 4.9, 7.2, 11.3, 18], [1.9, 3.4, 5.2, 9.3, 13]]

    labels = ["RFaas", "RFR", "KNN", "LR", "SVR", "MLP"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green"]

    plt.figure(figsize=(4, 3))
    bplot = plt.boxplot(float, patch_artist=True, labels=labels, positions=(0.1, 0.3, 0.5, 0.7, 0.9, 1.1),
                        widths=0.18)

    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    x_position = [0.6]
    x_position_fmt = ["float"]
    plt.xticks([i for i in x_position], x_position_fmt)
    plt.ylim(0, 20)
    plt.margins(0)

    plt.ylabel('预测失误率(%)')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.3, bottom=0.2)
    # plt.legend(bplot['boxes'], labels, loc='upper left', ncol=2)
    plt.savefig("box_float.pdf")
    plt.show()


def box_matmul():
    matmul = [[1.3, 3.2, 5.6, 6.1, 9.7], [1, 2.4, 4, 5.2, 8.5], [3, 4.7, 6.8, 8.3, 11], [3.3, 8, 12, 14, 18],
              [3.4, 9.2, 11.2, 14, 16], [2.3, 6.3, 9.2, 10.3, 14]]

    labels = ["RFaas", "RFR", "KNN", "LR", "SVR", "MLP"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green"]

    plt.figure(figsize=(4, 3))
    bplot = plt.boxplot(matmul, patch_artist=True, labels=labels, positions=(0.1, 0.3, 0.5, 0.7, 0.9, 1.1),
                        widths=0.18)

    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    x_position = [0.6]
    x_position_fmt = ["matmul"]
    plt.xticks([i for i in x_position], x_position_fmt)
    plt.ylim(0, 20)
    plt.margins(0)

    plt.ylabel('预测失误率(%)')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.3, bottom=0.2)
    # plt.legend(bplot['boxes'], labels, loc='upper left', ncol=2)
    plt.savefig("box_matmul.pdf")
    plt.show()


def box_social_network():
    social_network = [[60, 110, 125, 190, 270], [30, 60, 90, 105, 130], [40, 70, 105, 170, 200],
                      [130, 160, 180, 260, 290],
                      [79, 110, 140, 170, 190], [60, 90, 125, 180, 205]]

    labels = ["RFaas", "RFR", "KNN", "LR", "SVR", "MLP"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green"]

    plt.figure(figsize=(4, 3))
    bplot = plt.boxplot(social_network, patch_artist=True, labels=labels, positions=(0.1, 0.3, 0.5, 0.7, 0.9, 1.1),
                        widths=0.18)

    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    x_position = [0.6]
    x_position_fmt = ["SocialNetwork"]
    plt.xticks([i for i in x_position], x_position_fmt)
    plt.ylim(0, 300)
    plt.margins(0)

    plt.ylabel('预测失误率(%)')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(left=0.3, bottom=0.2)
    # plt.legend(bplot['boxes'], labels, loc='upper left', ncol=2)
    plt.savefig("box_social_network.pdf")
    plt.show()


def draw_legend():
    labels = ["RFaas", "RFR", "KNN", "LR", "SVR", "MLP"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green"]

    plt.figure(figsize=(14, 2))

    for i, (label, color) in enumerate(zip(labels, colors)):
        plt.bar(i, 0, color=color, label=label)

    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), ncol=len(labels))
    plt.axis('off')
    plt.subplots_adjust(bottom=0.4)
    plt.savefig("box_legend.pdf")
    plt.show()


def time_compare():
    # time_3000 = [0.0030045509338378906, 0.08678865432739258, 0.2196674346923828, 2.054060935974121,
    #              0.0009999275207519531]
    # time_4000 = [0.0040204524993896484, 0.13118457794189453, 0.41147565841674805, 2.7695670127868652,
    #              0.0015039443969726562]
    # time_5000 = [0.005621433258056641, 0.16290998458862305, 0.6436929702758789, 3.575896739959717,
    #              0.0015039443969726562]
    # time_6000 = [0.005512714385986328, 0.19843268394470215, 0.9779725074768066, 4.1641845703125, 0.0014252662658691406]
    # time_7000 = [0.006566286087036133, 0.2403852939605713, 1.3640694618225098, 4.949960231781006, 0.0010051727294921875]
    # time_8000 = [0.008948087692260742, 0.3287537097930908, 1.699087381362915, 5.56868314743042, 0.0010013580322265625]
    # time_9000 = [0.009514093399047852, 0.36073732376098633, 2.1725287437438965, 6.414708852767944,
    #              0.0009999275207519531]
    # time_10000 = [0.009509086608886719, 0.39911508560180664, 2.540026903152466, 6.77601170539856, 0.0009987354278564453]
    # time_20000 = [0.021145105361938477, 0.9211511611938477, 9.836096048355103, 13.880940437316895, 0.001504659652709961]
    # time_30000 = [0.029037952423095703, 1.6009109020233154, 22.403677463531494, 20.76758098602295, 0.001008749008178711]

    rfaas = [0.0009999275207519531, 0.0015039443969726562, 0.0015039443969726562, 0.0014252662658691406,
             0.0010051727294921875, 0.0010013580322265625, 0.0009999275207519531, 0.0009987354278564453,
             0.001504659652709961, 0.001008749008178711]
    lr = [0.0032776379585266113, 0.00750422477722168, 0.021849870681762695, 0.015984535217285156, 0.01749563217163086,
          0.02076554298400879, 0.024031400680541992, 0.026018381118774414, 0.02699732780456543, 0.03549790382385254]
    knn = [0.0030045509338378906, 0.0040204524993896484, 0.005621433258056641, 0.005512714385986328,
           0.006566286087036133, 0.008948087692260742, 0.009514093399047852, 0.009509086608886719, 0.021145105361938477,
           0.029037952423095703]
    rfr = [0.08678865432739258, 0.13118457794189453, 0.16290998458862305, 0.19843268394470215, 0.2403852939605713,
           0.3287537097930908, 0.36073732376098633, 0.39911508560180664, 0.9211511611938477, 1.6009109020233154]
    svc = [0.2196674346923828, 0.41147565841674805, 0.6436929702758789, 0.9779725074768066, 1.3640694618225098,
           1.699087381362915, 2.1725287437438965, 2.540026903152466, 9.836096048355103, 22.403677463531494]
    mlp = [2.054060935974121, 2.7695670127868652, 3.575896739959717, 4.1641845703125, 4.949960231781006,
           5.56868314743042, 6.414708852767944, 6.77601170539856, 13.880940437316895, 20.76758098602295]

    fig, ax = plt.subplots(1, 1, figsize=(6, 4))

    labels = ["3k", "4k", "5k", "6k", "7k", "8k", "9k", "10k", "20k", "30k"]
    ind = np.arange(len(labels))

    # ax.plot(ind, rfaas, marker='*', label='RFaas', linewidth=2)
    ax.plot(ind, knn, marker='o', label='KNN', linewidth=2)
    ax.plot(ind, lr, marker='*', label='LR', linewidth=2)
    ax.plot(ind, rfr, marker='.', label='RFR', linewidth=2)
    ax.plot(ind, svc, marker='+', label='SVC', linewidth=2)
    # ax.plot(ind, mlp, marker='s', label='MLP', linewidth=2)

    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    ax.tick_params(axis='both', which='major', labelsize=13, length=0)
    plt.margins(x=0)
    ax.legend(fontsize=13, loc="lower left", ncol=2)
    ax.set_xlabel('样本数量', labelpad=5, fontsize=13, fontproperties='SimSun')
    ax.set_ylabel('时间(s)', labelpad=5, fontsize=13, fontproperties='SimSun')
    # plt.title('CPU test')
    ax.grid(True, linestyle='--')

    axins = inset_axes(ax, width='65%', height='40%', loc='upper left', bbox_to_anchor=(0.1, 0, 1, 1),
                       bbox_transform=ax.transAxes)

    axins.plot(ind, knn, marker='o', label='KNN', linewidth=2)
    axins.plot(ind, lr, marker='*', label='LR', linewidth=2)
    axins.legend(fontsize=13)
    axins.set_xticks(ind)
    axins.set_xticklabels(labels)
    axins.tick_params(axis='both', which='major', labelsize=13, length=0)

    mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec='k', lw=1)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.2)
    plt.savefig("predictor_time_compare.pdf")
    plt.show()


if __name__ == '__main__':
    time_compare()
