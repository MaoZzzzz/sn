def split_file_by_target():
    data_filename = 'source.txt'
    target_filename = 'target.txt'

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


if __name__ == '__main__':
    # split_file_by_target()
    extract_column("x86_bak.txt", "x86_target.txt", 6)
    remove_column("x86_source.txt", "x86_source.txt", 6)
