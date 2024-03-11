import random


def split_file_by_target():
    data_filename = 'x86/source.txt'
    target_filename = 'x86/target.txt'

    with open(data_filename, 'r') as file:
        # 读取数据行，跳过标题行（如果有的话）
        data = file.read().strip().split('\n')[1:]  # 切片用于跳过标题行

    with open(target_filename, 'r') as file:
        # 读取目标行
        targets = file.read().strip().split('\n')[1:]

    # 检查数据和目标行的数量是否一致
    if len(data) != len(targets):
        print("数据行数和目标行数不一致，请检查文件！")
    else:
        # 将数据按照目标分类写入不同的文件
        for i, line in enumerate(data):
            target = targets[i].strip()
            filename = f"{target}.txt"
            with open(filename, 'a') as file:  # 使用追加模式'a'以保留以前的写入
                file.write(line + '\n')

        print("数据已经根据target值分类并写入到相应的文件中。")


def extract_column(input_file_path, output_file_path, i):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        with open(output_file_path, 'w') as output_file:
            for line in lines:
                columns = line.strip().split(',')
                output_file.write(columns[i] + '\n')


def remove_column(input_file_path, output_file_path, i):
    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    column_index = i
    modified_lines = []
    for line in lines:
        parts = line.strip().split(',')
        del parts[column_index]
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file_path, 'w') as f:
        f.writelines(modified_lines)


def modify_data(data, ratios):
    modified_data = []
    for i in range(len(data)):
        modified_row = []
        if isinstance(data[i], (int, float)):
            ratio = random.uniform(-ratios[i], ratios[i])
            modified_value = data[i] + data[i] * ratio
            if modified_value < 0:
                modified_value = modified_value * -1
            modified_row.append(modified_value)

        modified_data.append(modified_row)
    return modified_data


def completion_column(input_file_path, output_file_path):
    cpu_idle = [86.00, 68.40, 45.08, 62.09, 65.01, 68.34, 64.45, 64.11, 64.34, 1.81]
    disk = [553.33, 1376.89, 1082.10, 1681.33, 1552.00, 1402.00, 6407.49, 5425.81, 1251.36, 856.37]
    network = [583.83, 1260.89, 380.96, 583.33, 700.60, 1205.99, 521.74, 540.20, 857.66, 19.33]
    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    index = 0
    num = 0
    for line in lines:
        if num < 100:
            num += 1
        else:
            num = 0
            index += 1
        parts = line.strip().split(',')
        cpu = cpu_idle[index] * random.uniform(-0.1, 0.1) + cpu_idle[index]
        d = disk[index] * random.uniform(-0.1, 0.1) + disk[index]
        n = network[index] * random.uniform(-0.1, 0.1) + network[index]
        parts.append(str(round(cpu, 2)))
        parts.append(str(round(d, 2)))
        parts.append(str(round(n, 2)))
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file_path, 'w') as f:
        f.writelines(modified_lines)


# branches,branch-misses,context-switches,cpu-clock,cpu-migrations,page-faults,cpu-idle,disk-io,network-bandwidth

if __name__ == '__main__':
    completion_column("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\source.txt",
                      "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\x86\\full_source.txt")
    # split_file_by_target()
    # extract_column("x86_bak.txt", "x86_target.txt", 6)
    # remove_column("D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\source.txt",
    #               "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\source.txt", 5)
