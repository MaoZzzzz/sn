import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False


def box():
    data = [[60, 110, 125, 190, 270], [30, 60, 90, 105, 130], [40, 70, 105, 170, 200],
            [130, 160, 180, 260, 290],
            [79, 110, 140, 170, 190], [60, 90, 125, 180, 205]]

    labels = ["RFaas", "RFR", "KNN", "LR", "SVR", "MLP"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green"]

    plt.figure(figsize=(4, 3))
    bplot = plt.boxplot(data, patch_artist=True, labels=labels, positions=(0.1, 0.3, 0.5, 0.7, 0.9, 1.1),
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
    # plt.savefig("box_social_network.pdf")
    plt.show()


def box_sub():
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(9, 6))
    plt.subplots_adjust(hspace=0.5, wspace=0.4)

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\time_result\knn_predict_time.txt",
              'r') as file:
        riscv_knn_lines = file.readlines()
    riscv_knn = [float(line.strip()) for line in riscv_knn_lines]
    groups_knn_riscv = [riscv_knn[i:i + 20] for i in range(0, len(riscv_knn), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\time_result\\rfr_predict_time.txt",
              'r') as file:
        riscv_rfr_lines = file.readlines()
    riscv_rfr = [float(line.strip()) for line in riscv_rfr_lines]
    groups_rfr_riscv = [riscv_rfr[i:i + 20] for i in range(0, len(riscv_rfr), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\time_result\lr_predict_time.txt",
              'r') as file:
        riscv_lr_lines = file.readlines()
    riscv_lr = [float(line.strip()) for line in riscv_lr_lines]
    groups_lr_riscv = [riscv_lr[i:i + 20] for i in range(0, len(riscv_lr), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\draw\mlp_predict_time.txt",
              'r') as file:
        riscv_mlp_lines = file.readlines()
    riscv_mlp = [float(line.strip()) for line in riscv_mlp_lines]
    groups_mlp_riscv = [riscv_mlp[i:i + 5] for i in range(0, len(riscv_mlp), 5)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\draw\svr_predict_time.txt",
              'r') as file:
        riscv_svr_lines = file.readlines()
    riscv_svr = [float(line.strip()) for line in riscv_svr_lines]
    groups_svr_riscv = [riscv_svr[i:i + 5] for i in range(0, len(riscv_svr), 5)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\time_result\knn_predict_time.txt",
              'r') as file:
        riscv_knn_lines = file.readlines()
    riscv_knn = [float(line.strip()) for line in riscv_knn_lines]
    groups_knn_x86 = [riscv_knn[i:i + 20] for i in range(0, len(riscv_knn), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\time_result\\rfr_predict_time.txt",
              'r') as file:
        riscv_rfr_lines = file.readlines()
    riscv_rfr = [float(line.strip()) for line in riscv_rfr_lines]
    groups_rfr_x86 = [riscv_rfr[i:i + 20] for i in range(0, len(riscv_rfr), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\time_result\lr_predict_time.txt",
              'r') as file:
        riscv_lr_lines = file.readlines()
    riscv_lr = [float(line.strip()) for line in riscv_lr_lines]
    groups_lr_x86 = [riscv_lr[i:i + 20] for i in range(0, len(riscv_lr), 20)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\draw\mlp_predict_time.txt",
              'r') as file:
        riscv_mlp_lines = file.readlines()
    riscv_mlp = [float(line.strip()) for line in riscv_mlp_lines]
    groups_mlp_x86 = [riscv_mlp[i:i + 5] for i in range(0, len(riscv_mlp), 5)]

    with open("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\draw\svr_predict_time.txt",
              'r') as file:
        riscv_svr_lines = file.readlines()
    riscv_svr = [float(line.strip()) for line in riscv_svr_lines]
    groups_svr_x86 = [riscv_svr[i:i + 5] for i in range(0, len(riscv_svr), 5)]

    labels = ["RFR_RISCV", "RFR_X86", "KNN_RISCV", "KNN_X86", "LR_RISCV", "LR_X86", "SVR_RISCV", "SVR_X86"]
    colors = ["firebrick", "dimgrey", "dodgerblue", "blueviolet", "gold", "green", "#8B7500", "#6959CD"]
    functionName = ["compose-post", "upload-creator", "upload-text", "upload-media", "upload-unique-id",
                    "upload-user-mentions", "post-storage", "upload-home-timeline", "upload-user-timeline", "matmul"]

    for i, ax in enumerate(axes.flatten()):
        data = []
        data.append(groups_rfr_riscv[i])
        data.append(groups_rfr_x86[i])
        data.append(groups_knn_riscv[i])
        data.append(groups_knn_x86[i])
        data.append(groups_lr_riscv[i])
        data.append(groups_lr_x86[i])
        data.append(groups_svr_riscv[i])
        data.append(groups_svr_x86[i])
        # data.append(groups_mlp_riscv[i])
        # data.append(groups_mlp_x86[i])

        bplot = ax.boxplot(data, patch_artist=True, labels=labels,
                           positions=(0.1, 0.3, 0.8, 1.0, 1.5, 1.7, 2.2, 2.4),
                           widths=0.18, showfliers=False)

        x_position = [0.25, 0.95, 1.65, 2.35]
        x_position_fmt = ["RFR", "KNN", "LR", "SVR"]

        font_dict = {'fontname': 'Times New Roman', 'fontsize': 13}
        ax.set_title(functionName[i], fontsize=13, fontproperties='Times New Roman')
        ax.set_xticks(x_position)
        ax.set_xticklabels(x_position_fmt, fontdict=font_dict)

        ax.tick_params(axis='both', labelsize=13)

        if i == 0 or i == 3 or i == 6:
            ax.set_ylabel("预测时间", fontsize=13, fontproperties='SimSun')

        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        ax.margins(0)

    plt.savefig("box_predict_time.pdf")
    plt.show()


def error_num(x86_file_path, riscv_file_path, index):
    with open(x86_file_path, 'r') as f:
        x86_lines = f.readlines()
    with open(riscv_file_path, 'r') as f:
        riscv_lines = f.readlines()

    x86_rfr = [float(line.strip()) for line in x86_lines]
    groups_rfr_x86 = [x86_rfr[i:i + 20] for i in range(0, len(x86_rfr), 20)]

    riscv_rfr = [float(line.strip()) for line in riscv_lines]
    groups_rfr_riscv = [riscv_rfr[i:i + 20] for i in range(0, len(riscv_rfr), 20)]

    sum = 0
    for i in range(len(groups_rfr_riscv[index])):
        print(groups_rfr_riscv[index][i])
        print(groups_rfr_x86[index][i])
        if groups_rfr_riscv[index][i] > groups_rfr_x86[index][i]:
            sum += 1

    print(sum / 20)


if __name__ == '__main__':
    box_sub()
    # error_num("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\time_result\\rfr_predict_time.txt",
    #           "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\time_result\\rfr_predict_time.txt", 8)
