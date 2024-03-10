import os


def run(file_path):
    # file_full_path = 'D:\\Workdir\\idea\\Schedule\\data\\stage2\\format\\{}'.format(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # result_map = {'dummy': 0.0, 'branch-misses': 0.0, 'ns': 0.0, 'emulation-faults': 0.0, 'cpu-migrations': 0.0,
    #               'msec': 0.0,
    #               'page-faults': 0.0, 'context-switches': 0.0, 'branches': 0.0}

    result_map = {'branch-misses': 0.0, 'cpu-migrations': 0.0, 'cpu-clock': 0.0,
                  'page-faults': 0.0, 'context-switches': 0.0, 'branches': 0.0}

    index = 0
    for line in lines:
        key, value = line.strip().split(" ")[:2]
        if key == 'dummy' or key == 'ns' or key == 'emulation-faults':
            continue
        if key == 'branch-misses':
            index = index + 1
        if key == 'msec':
            key = "cpu-clock"
        result_map[key] = result_map.get(key) + float(value)

    values = list(result_map.values())
    for i in range(len(values)):
        if index == 0:
            break
        values[i] = values[i] / index

    print(file_path)
    print(result_map.keys())
    print(values)


# folder_path = 'D:\\Workdir\\idea\\Schedule\\data\\stage2\\format'
#
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         file_path = os.path.join(root, file)
#
#         # 检查文件名前缀和路径中是否包含 "X86"
#         if file.startswith("perf") and "X86" in file_path:
#             run(file_path)

input_files = ['riscv_bak.txt', 'riscv_bak.txt']

with open("1.txt", 'r') as output:
    file1 = output.readlines()

with open("2.txt", 'r') as output:
    file2 = output.readlines()

with open("3.txt", 'w') as output:
    for i in range(len(file1)):
        output.write(file1[i].strip() + "," + file2[i])
