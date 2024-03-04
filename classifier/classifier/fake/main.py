import random


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


def evening_the_correlation(file_nums, add_nums):
    columns = [[] for _ in range(11)]

    with open('source.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            for i in range(11):
                columns[i].append(parts[i])

    ratios = [0.3, 1, 1, 1, 1, 0.3, 0.3, 0, 0.3, 1, 1]
    random_numbers = [random.randint(1, file_nums) for _ in range(add_nums)]

    file_path_source = 'source.txt'
    file_path_target = 'target.txt'

    with open(file_path_source, 'r') as file:
        lines_source = file.readlines()

    with open(file_path_target, 'r') as file:
        lines_target = file.readlines()

    for i in range(len(random_numbers)):
        new_row = []
        for j in range(len(columns)):
            new_row.append(float(random.choice(columns[j])) * ratios[j])
        # new_row = [random.choice(column) for column in columns]
        new_row[7] = columns[7][i]
        new_row_str = [str(element) for element in new_row]
        source = ','.join(new_row_str) + "\n"
        target = "1" + "\n" if lines_target[random_numbers[i]] == "1" else "0" + "\n"

        lines_source.insert(random_numbers[i], source)
        lines_target.insert(random_numbers[i], target)

        with open(file_path_source, 'w') as file:
            file.writelines(lines_source)
        with open(file_path_target, 'w') as file:
            file.writelines(lines_target)


def modify_system_call_colume():
    input_file = 'source.txt'
    output_file = 'source.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    column_index = 7
    for line in lines:
        parts = line.strip().split(',')
        # parts[column_index] = '0.0'
        if float(parts[column_index]) > 0 and float(parts[column_index]) < 50:
            parts[column_index] = str("67.0")
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)


def add_some_error(file_nums, add_nums):
    columns = [[] for _ in range(11)]

    with open('source.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            for i in range(11):
                columns[i].append(parts[i])

    ratios = [0.3, 1, 1, 1, 1, 0.3, 0.3, 0, 0.3, 1, 1]
    random_numbers = [random.randint(1, file_nums) for _ in range(add_nums)]

    file_path_source = 'source.txt'
    file_path_target = 'target.txt'

    with open(file_path_source, 'r') as file:
        lines_source = file.readlines()

    with open(file_path_target, 'r') as file:
        lines_target = file.readlines()

    for i in range(len(random_numbers)):
        target = "0" + "\n" if lines_target[random_numbers[i]] == "1" else "1" + "\n"

        new_row = []
        for j in range(len(columns)):
            new_row.append(float(random.choice(columns[j])) * ratios[j])
        # new_row = [random.choice(column) for column in columns]

        if target == "1\n":
            new_row[7] = "67.0"
        elif target == "0\n":
            new_row[7] = "0"

        new_row_str = [str(element) for element in new_row]
        source = ','.join(new_row_str) + "\n"

        lines_source.insert(random_numbers[i], source)
        lines_target.insert(random_numbers[i], target)

        with open(file_path_source, 'w') as file:
            file.writelines(lines_source)
        with open(file_path_target, 'w') as file:
            file.writelines(lines_target)


def remove_column(i):
    input_file = 'source_wo_system_call.txt'
    output_file = 'source_wo_system_call.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()

    column_index = i
    modified_lines = []
    for line in lines:
        parts = line.strip().split(',')
        del parts[column_index]
        modified_lines.append(','.join(parts) + '\n')

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)


if __name__ == "__main__":
    # evening_the_correlation(0, 0)
    # add_some_error(1900, 300)
    # modify_system_call_colume()
    remove_column(8)
