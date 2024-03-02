import random
import csv


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


def run1():
    # latency, call percent, cpu idle, io write, 每秒收包, 每秒发包
    # branch-misses,cpu-migrations,cpu-clock,page-faults,context-switches,branches,latency,call-percent,cpu-idle,disk-io,network-bandwidth
    # format_data = [
    #     [0.000094392299, 0, 86.00, 553.33, 417.50, "X86"],
    #     [0.004816651344, 60, 68.40, 1376.89, 1371.22, "RISCV"],
    #     [0.004058515071, 68, 68.34, 1402.00, 1314.76, "RISCV"],
    #     [0.000100575447, 0, 45.08, 1082.10, 272.36, "X86"],
    #     [0.000130791187, 0, 62.09, 1681.33, 417.17, "X86"],
    #     [0.000100461483, 0, 65.01, 1552.00, 501.00, "X86"],
    #     [0.000177340984, 0, 65.24, 1656.00, 499.80, "X86"],
    #     [0.015103614332, 67, 64.45, 6407.49, 519.86, "RISCV"],
    #     [0.024893628120, 75, 64.11, 5425.81, 582.23, "RISCV"],
    #     [0.011684287548, 39, 64.34, 1251.36, 891.34, "RISCV"],
    #     [298.32, 0, 9.81, 856.37, 14.14, "X86"],
    #     [1.78869, 0, 22.54, 331.45, 34.11, "X86"],
    # ]

    format_data = [
        [0, 86.00, 553.33, 417.50, "X86"],
        [60, 68.40, 1376.89, 1371.22, "RISCV"],
        [68, 68.34, 1402.00, 1314.76, "RISCV"],
        [0, 45.08, 1082.10, 272.36, "X86"],
        [0, 62.09, 1681.33, 417.17, "X86"],
        [0, 65.01, 1552.00, 501.00, "X86"],
        [0, 65.24, 1656.00, 499.80, "X86"],
        [67, 64.45, 6407.49, 519.86, "RISCV"],
        [75, 64.11, 5425.81, 582.23, "RISCV"],
        [39, 64.34, 1251.36, 891.34, "RISCV"],
        [0, 9.81, 856.37, 14.14, "X86"],
        [0, 22.54, 331.45, 34.11, "X86"],
    ]

    # Ratios for modification
    ratios = [0, 0.3, 0.1, 0.1, 0]

    index = [49, 49, 56, 47, 50, 49, 49]
    index_2 = [0, 7, 1, 3, 4, 2, 11]
    index_3 = [0, 49, 98, 154, 201, 251, 300, 351]

    with open("merged_file_bak.txt", 'r') as file:
        lines = file.readlines()

    new_lines = []
    for i in range(len(index)):
        for j in range(index_3[i], index_3[i] + index[i]):
            data = modify_data(format_data[index_2[i]], ratios)
            formatted_data = [','.join(map(str, sublist)) for sublist in data]
            output_string = ','.join(formatted_data)
            output_string = output_string[0:len(output_string) - 1]
            print(lines[j])
            line = lines[j].strip() + "," + output_string + "\n"
            new_lines.append(line)

    with open("merged_file.txt", 'w') as file:
        file.writelines(new_lines)


def run2():
    ratios = [3.0, 2, 3.0, 1, 1, 3.0, 3.0, 0, 3.0, 3.0, 3.0]
    random_numbers = [random.randint(1, 600) for _ in range(600)]

    file_path_source = 'source.txt'
    file_path_target = 'target.txt'

    for i in range(len(random_numbers)):
        with open(file_path_source, 'r') as file:
            lines_source = file.readlines()
            temp = [float(element) for element in lines_source[random_numbers[i]].split(",")]
            formatted_data = [','.join(map(str, sublist)) for sublist in modify_data(temp, ratios)]
            source = ','.join(formatted_data) + "\n"

        with open(file_path_target, 'r') as file:
            lines_target = file.readlines()
            target = "1" + "\n" if lines_target[random_numbers[i]] == "1" else "0" + "\n"
            # if random_numbers[i] / 2 == 0:
            #     target = "0" + "\n" if lines_target[random_numbers[i]] == "1" else "1" + "\n"
            # else:
            #     target = "1" + "\n" if lines_target[random_numbers[i]] == "1" else "0" + "\n"

        lines_source.insert(random_numbers[i], source)
        lines_target.insert(random_numbers[i], target)

        with open(file_path_source, 'w') as file:
            file.writelines(lines_source)
        with open(file_path_target, 'w') as file:
            file.writelines(lines_target)


def remove_system_call():
    input_file = 'source.txt'
    output_file = 'source_wo_system_call.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()

    column_index = 7
    modified_lines = []
    for line in lines:
        parts = line.strip().split(',')
        del parts[column_index]
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)


def modify_system_call():
    input_file = 'source_wo_system_call.txt'
    output_file = 'source_wo_system_call.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    column_index = 10
    for line in lines:
        parts = line.strip().split(',')
        parts[column_index] = str("0")
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)


def modify_system_call_colume():
    input_file = 'source_wo_system_call.txt'
    output_file = 'source_wo_system_call.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    column_index = 7
    for line in lines:
        parts = line.strip().split(',')
        if float(parts[column_index]) > 0 and float(parts[column_index]) < 50:
            parts[column_index] = str("67.0")
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)


if __name__ == "__main__":
    # run2()
    modify_system_call_colume()
