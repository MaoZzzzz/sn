import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau


def read_from_file(i):
    # 读取第一个文件
    file1_path = 'D:\Workdir\pycharm\sn\classifier\classifier\stage2\\x86_source.txt'
    df1 = pd.read_csv(file1_path, header=None)

    # 读取第二个文件
    file2_path = 'D:\Workdir\pycharm\sn\classifier\classifier\stage2\\x86_target.txt'
    df2 = pd.read_csv(file2_path, header=None)

    pearsonr_corr, pearsonr_p_value = pearsonr(df1[i], df2[0])
    kendall_corr, kendall_p_value = kendalltau(df1[i], df2[0])
    spearman_corr, spearman_p_value = spearmanr(df1[i], df2[0])
    print(f"Pearson Correlation Coefficient for column : {pearsonr_corr, pearsonr_p_value}")
    # print(f"Kendalltau Correlation Coefficient for column : {kendall_corr, kendall_p_value}")
    # print(f"Spearmanr Correlation Coefficient for column : {spearman_corr, spearman_p_value}")


def read_from_data():
    # format_data = [
    #     [0.000094392299, 0, 86.00, 553.33, 417.50, 583.83, "X86"],
    #     [0.004816651344, 60, 68.40, 1376.89, 1371.22, 1260.89, "RISCV"],
    #     [0.004058515071, 68, 68.34, 1402.00, 1314.76, 1205.99, "RISCV"],
    #     [0.000100575447, 0, 45.08, 1082.10, 272.36, 380.96, "X86"],
    #     [0.000130791187, 0, 62.09, 1681.33, 417.17, 583.33, "X86"],
    #     [0.000100461483, 0, 65.01, 1552.00, 501.00, 700.60, "X86"],
    #     [0.000177340984, 0, 65.24, 1656.00, 499.80, 699.60, "X86"],
    #     [0.015103614332, 67, 64.45, 6407.49, 519.86, 521.74, "RISCV"],
    #     [0.024893628120, 75, 64.11, 5425.81, 582.23, 540.20, "RISCV"],
    #     [0.011684287548, 39, 64.34, 1251.36, 891.34, 857.66, "RISCV"],
    #     [298.32, 0, 9.81, 856.37, 14.14, 19.33, "X86"],
    # ]
    format_data = [
        [0.000094392299, 0, 86.00, 553.33, 417.50, 583.83, "0"],
        [0.004816651344, 60, 68.40, 1376.89, 1371.22, 1260.89, "1"],
        [0.004058515071, 68, 68.34, 1402.00, 1314.76, 1205.99, "1"],
        [0.000100575447, 0, 45.08, 1082.10, 272.36, 380.96, "0"],
        [0.000130791187, 0, 62.09, 1681.33, 417.17, 583.33, "0"],
        [0.000100461483, 0, 65.01, 1552.00, 501.00, 700.60, "0"],
        [0.000177340984, 0, 65.24, 1656.00, 499.80, 699.60, "0"],
        [0.015103614332, 67, 64.45, 6407.49, 519.86, 521.74, "1"],
        [0.024893628120, 75, 64.11, 5425.81, 582.23, 540.20, "1"],
        [0.011684287548, 39, 64.34, 1251.36, 891.34, 857.66, "1"],
        [298.32, 0, 9.81, 856.37, 14.14, 19.33, "0"],
    ]
    x = np.array(format_data)[:, len(format_data[0]) - 1].astype(float)
    for i in range(0, len(format_data[0])):
        y = np.array(format_data)[:, i].astype(float)
        pearsonr_corr, pearsonr_p_value = pearsonr(x, y)
        kendall_corr, kendall_p_value = kendalltau(x, y)
        spearman_corr, spearman_p_value = spearmanr(x, y)
        print(f"Pearson Correlation Coefficient for column {i + 1}: {pearsonr_corr, pearsonr_p_value}")
        print(f"Kendalltau Correlation Coefficient for column {i + 1}: {kendall_corr, kendall_p_value}")
        print(f"Spearmanr Correlation Coefficient for column {i + 1}: {spearman_corr, spearman_p_value}")


if __name__ == "__main__":
    for i in range(0, 10):
        read_from_file(i)
