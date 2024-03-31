import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']

file_path = 'data.txt'  # Replace with your actual file path


def one_plt():
    # Read data from file
    with open(file_path, 'r') as file:
        data_lines = file.readlines()

    # Process data
    data_list = [line.strip().split(',') for line in data_lines if line.strip() and len(line.strip().split(',')) == 3]
    df = pd.DataFrame(data_list, columns=['Operation', 'Column1', 'Column2'])
    df['Column1'] = df['Column1'].apply(lambda x: float(x.strip('<>')))
    df['Column2'] = df['Column2'].apply(lambda x: float(x.strip('<>')))

    # Normalize data
    df['Normalized'] = df['Column2'] / df['Column1']
    df['one'] = 1

    plt.figure(figsize=(6, 3))
    bar_width = 0.8
    opacity = 0.8

    plt.bar(df.index, df['one'], bar_width, alpha=opacity, label='X86', edgecolor='black')
    plt.bar(df.index + bar_width, df['Normalized'], bar_width, alpha=opacity, label='RISCV', edgecolor='black')

    plt.xticks(df.index + bar_width / 2, df['Operation'], rotation=90, fontproperties='Times New Roman')
    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)

    plt.legend(fontsize=8)
    plt.ylabel('归一化结果', labelpad=5)
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.4)
    plt.savefig("system_call_compare.pdf")

    plt.show()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))


def two_subpicture():
    # Read data from file
    with open(file_path, 'r') as file:
        data_lines = file.readlines()

    # Process data
    data_list = [line.strip().split(',') for line in data_lines if line.strip() and len(line.strip().split(',')) == 3]
    df = pd.DataFrame(data_list, columns=['Operation', 'Column1', 'Column2'])
    df['Column1'] = df['Column1'].apply(lambda x: float(x.strip('<>')))
    df['Column2'] = df['Column2'].apply(lambda x: float(x.strip('<>')))

    # Normalize data and split into two halves
    df_half1 = df.iloc[:len(df) // 2]
    df_half2 = df.iloc[len(df) // 2:]
    df_half1['Normalized'] = df_half1['Column2'] / df_half1['Column1']
    df_half2['Normalized'] = df_half2['Column2'] / df_half2['Column1']
    df_half1['one'] = 1
    df_half2['one'] = 1

    # 创建两个子图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
    bar_width = 0.8
    opacity = 0.8

    # 绘制第一个子图
    ax1.bar(df_half1.index, df_half1['one'], bar_width, alpha=opacity, label='X86', edgecolor='black')
    ax1.bar(df_half1.index, df_half1['Normalized'], bar_width, alpha=opacity, label='RISCV',
            edgecolor='black')
    ax1.set_xticks(df_half1.index)
    ax1.set_xticklabels(df_half1['Operation'], rotation=90)
    ax1.tick_params(axis='both', which='major', labelsize=8, length=0)
    ax1.margins(x=0)
    ax1.legend(fontsize=8)
    ax1.set_ylabel('归一化结果', labelpad=5)
    ax1.grid(True, linestyle='--')

    # 绘制第二个子图
    ax2.bar(df_half2.index, df_half2['one'], bar_width, alpha=opacity, label='X86', edgecolor='black')
    ax2.bar(df_half2.index, df_half2['Normalized'], bar_width, alpha=opacity, label='RISCV',
            edgecolor='black')
    ax2.set_xticks(df_half2.index)
    ax2.set_xticklabels(df_half2['Operation'], rotation=90)
    ax2.tick_params(axis='both', which='major', labelsize=8, length=0)
    ax2.margins(x=0)
    ax2.legend(fontsize=8)
    ax2.set_xlabel('系统调用名称', labelpad=5)
    ax2.set_ylabel('归一化结果', labelpad=5)
    ax2.grid(True, linestyle='--')

    # 调整子图之间的垂直间距
    plt.subplots_adjust(hspace=0.8, bottom=0.25)

    # 保存图形
    plt.savefig("system_call_compare.pdf")

    # 显示图形
    plt.show()


if __name__ == "__main__":
    two_subpicture()
