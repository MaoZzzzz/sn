data_file_path = "D:\\Workdir\\idea\\Schedule\\data\\format\\aluResult.txt"

category_sums = {}

with open(data_file_path, 'r') as file:
    for line in file:
        # 拆分每行数据
        parts = line.strip().split()

        # 提取 string 和 float
        string_value = parts[1]
        float_value = float(parts[2])

        # 将 float 累加到对应 string 的总和中
        if string_value in category_sums:
            category_sums[string_value] += float_value
        else:
            category_sums[string_value] = float_value

# 打印每个 string 对应的总和
for category, total_sum in category_sums.items():
    print(f'{category}: {total_sum}')

categories = list(category_sums.keys())
total_sums = list(category_sums.values())

for i in range(len(total_sums)):
    total_sums[i] = total_sums[i] / 4

print(categories)
print(total_sums)

array1 = ['gettid', 'ioctl', 'getrandom', 'write', 'fstat', 'close', 'read', 'set_robust_list', 'lseek', 'getsockname',
          'stat', 'socketpair', 'openat', 'exit_group', 'brk', 'clone', 'getpid', 'wait4', 'pipe2', 'prlimit64',
          'munmap', 'mmap', 'mprotect']
array2 = ['ioctl', 'openat', 'gettid', 'lseek', 'close', 'newfstatat', 'set_robust_list', 'getrandom', 'write',
          'exit_group', 'prlimit64', 'mmap', 'brk', 'read', 'getsockname', 'wait4', 'getpid', 'mprotect', 'munmap',
          'clone', 'socketpair', 'pipe2']

set1 = set(array1)
set2 = set(array2)

common_elements = set1.intersection(set2)
different_elements = set1.symmetric_difference(set2)

print("Common Elements:", list(common_elements))
print("Different Elements:", list(different_elements))
