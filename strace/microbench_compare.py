import matplotlib.pyplot as plt
import numpy as np


def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        if line.startswith('BM_'):
            parts = line.split()
            name = parts[0][3:]  # 去掉BM_
            time = float(parts[3])  # 选择第二列的时间
            data[name] = time

    return data


def compare_and_plot(file1_path, file2_path):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    data1 = read_data(file1_path)
    data2 = read_data(file2_path)

    names = list(set(data1.keys()) | set(data2.keys()))
    names.sort()

    times1 = [data1.get(name, 0) for name in names]
    times2 = [data2.get(name, 0) for name in names]

    width = 0.9
    ind = np.arange(len(names))

    plt.figure(figsize=(4, 3))

    plt.bar(ind - width / 4, times1, width / 2, label='X86', edgecolor='black')
    plt.bar(ind + width / 4, times2, width / 2, label='RISCV', edgecolor='black')

    names = ['AND', 'BEQZ', 'BITS_AND', 'BITS_LSHIFT', 'BITS_NOR', 'BITS_NOT', 'BITS_OR', 'BITS_RSHIFT', 'BNEZ',
             'BML_BEQZ', 'BML_BNEZ', 'BUBBLE_SORT', 'CBML_BEQZ', 'CBML_BNEZ', 'CML_BEQZ', 'CML_BNEZ', 'DEC', 'DIV',
             'DO_WHILE_LOOP', 'FLOAT_DEC', 'FLOAT_DIV', 'FLOAT_INC', 'FLOAT_MUL', 'FOR_LOOP', 'INC', 'LOAD_BEQZ',
             'LOAD_BNEZ', 'MUL', 'NOP', 'NOT', 'OR', 'STD_SORT', 'UB', 'WHILE_LOOP']

    plt.xticks(ind, names, rotation=90)
    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)

    plt.legend(fontsize=8)
    plt.xlabel('函数名')
    plt.ylabel('时间 (纳秒)', labelpad=5)
    # plt.title('CPU test')
    plt.grid(True, linestyle='--')
    plt.subplots_adjust(bottom=0.3)
    plt.savefig("microbench_compare.pdf")

    plt.show()


def normalization(file1_path, file2_path):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    data1 = read_data(file1_path)
    data2 = read_data(file2_path)

    names = list(set(data1.keys()) | set(data2.keys()))
    names.sort()

    # times1 = [data1.get(name, 0) for name in names]
    times1 = np.ones(len(names))
    times2 = [data2.get(name, 0) / data1.get(name, 0) for name in names]

    bar_width = 0.8
    opacity = 0.8
    ind = np.arange(len(names))

    plt.figure(figsize=(4, 3))

    plt.bar(ind, times1, bar_width, alpha=opacity, label='X86', edgecolor='black')
    plt.bar(ind, times2, bar_width, alpha=opacity, label='RISCV',
            edgecolor='black')
    names = ['AND', 'BEQZ', 'BITS_AND', 'BITS_LSHIFT', 'BITS_NOR', 'BITS_NOT', 'BITS_OR', 'BITS_RSHIFT', 'BNEZ',
             'BML_BEQZ', 'BML_BNEZ', 'BUBBLE_SORT', 'CBML_BEQZ', 'CBML_BNEZ', 'CML_BEQZ', 'CML_BNEZ', 'DEC', 'DIV',
             'DO_WHILE_LOOP', 'FLOAT_DEC', 'FLOAT_DIV', 'FLOAT_INC', 'FLOAT_MUL', 'FOR_LOOP', 'INC', 'LOAD_BEQZ',
             'LOAD_BNEZ', 'MUL', 'NOP', 'NOT', 'OR', 'STD_SORT', 'UB', 'WHILE_LOOP']
    plt.xticks(ind, names, rotation=90)
    plt.tick_params(axis='both', which='major', labelsize=8, length=0)
    plt.margins(x=0)
    plt.legend(fontsize=8)
    plt.xlabel('函数名称', labelpad=5)
    plt.ylabel('归一化结果', labelpad=5)
    plt.grid(True, linestyle='--')

    plt.subplots_adjust(bottom=0.35)
    # plt.savefig("microbench_compare.pdf")

    plt.show()


if __name__ == "__main__":
    normalization('D:\\Workdir\\pycharm\\sn\\strace\\microbench_riscv.txt',
                  'D:\\Workdir\\pycharm\\sn\\strace\\microbench_x86.txt')
    # compare_and_plot('D:\\Workdir\\pycharm\\sn\\strace\\microbench_riscv.txt',
    #                  'D:\\Workdir\\pycharm\\sn\\strace\\microbench_x86.txt')
