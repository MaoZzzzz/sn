import matplotlib.pyplot as plt

# 读取文件
filename = 'D:\\Workdir\\idea\\Schedule\\data\\format\\upload-creator-RISCV.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

# 初始化字典，用于存储每个名字对应的时间总和
name_to_time = {}

# 遍历文件行
for line in lines:
    parts = line.split()

    # 如果是 StartTime&&EndTime 行，则获取开始和结束时间
    if parts[0] == "StartTime&&EndTime:":
        start_time = float(parts[1])
        end_time = float(parts[2])
        total_time_diff = end_time - start_time
        break  # 假设 StartTime&&EndTime 行是文件的最后一行，直接跳出循环

    # 否则，按照第一部分和第二部分的名字进行分类，将时间累加
    name = f"{parts[0]} {parts[1]}"
    time = float(parts[2])
    if name in name_to_time:
        name_to_time[name] += time
    else:
        name_to_time[name] = time

# 提取名字和时间和数组
names = list(name_to_time.keys())
times = list(name_to_time.values())

# 打印总时间差和名字、时间和数组
print(f'Total Time Difference: {total_time_diff} seconds')
print('Names:', names)
print('Times:', times)

name_prefix_to_times = {}

# 遍历 Names 和 Times 数组，按照名字前半部分进行分类
for name, time in zip(names, times):
    name_prefix = name.split(' ')[0]
    if name_prefix in name_prefix_to_times:
        name_prefix_to_times[name_prefix]['Names'].append(name.split(" ")[1])
        name_prefix_to_times[name_prefix]['Times'].append(time)
    else:
        name_prefix_to_times[name_prefix] = {'Names': [name.split(" ")[1]], 'Times': [time]}

# 打印每个名字前半部分对应的名字和时间数组
for prefix, data in name_prefix_to_times.items():
    print(f'Name Prefix: {prefix}')
    print('Names:', data['Names'])
    print('Times:', data['Times'])
    print()

name = ['newfstatat', 'getpeername', 'getsockname', 'mprotect', 'rt_sigprocmask', 'recvfrom', 'clone', 'getpid',
        'getsockopt', 'clock_gettime', 'ppoll', 'gettid', 'close', 'setsockopt', 'connect', 'ioctl', 'mmap', 'fcntl',
        'getrandom', 'sendto', 'futex', 'munmap', 'socket']
time = [0.000563, 4.5e-05, 4.7e-05, 0.000117, 0.001155, 0.013272, 0.001059, 0.000829, 0.000931, 0.016806, 0.000433,
        0.000527, 8.3e-05, 0.00115, 0.001647, 0.00103, 0.001111, 0.000596, 9.5e-05, 0.000605, 0.041853, 0.00066,
        0.001183]

name2 = ['recvfrom', 'socket', 'getpid', 'gettid', 'mmap', 'fcntl', 'setsockopt', 'futex', 'connect', 'sendto',
         'getsockopt', 'rt_sigprocmask', 'clock_nanosleep', 'clock_gettime', 'ppoll', 'ioctl']
time2 = [0.000356, 0.000287, 0.00032, 0.000333, 0.000294, 0.000382, 0.0014, 0.015701, 0.000513, 0.000544, 0.001254,
         0.000356, 0.0, 0.006955, 0.001362, 0.000791]

a = 0
for i in range(len(time)):
    a += time[i]
a = 0.3402421

# 绘制柱状图
# plt.bar([1], [a], color='blue', label='a')

for i in range(len(time)):
    if (i != 0):
        plt.bar("1", time[i], bottom=time[i - 1])
    else:
        plt.bar("1", time[i])

for i in range(len(time2)):
    if (i != 0):
        plt.bar("2", time2[i], bottom=time2[i - 1])
    else:
        plt.bar("2", time2[i])

plt.bar("3", a)
# plt.bar("1", a, bottom=time[len(time) - 1])
# # 在柱子上标记 time 数组的数据段
# start_x = 1  # 柱子的 x 坐标
# for i, time_value in enumerate(times):
#     plt.text(start_x, a + 0.01, f"{time_value:.4f}", ha='center', va='bottom')
#     start_x += 1

# 设置图表标题和标签
plt.title('Bar Chart with Time Markings')
plt.xlabel('Names')
plt.ylabel('Values')

# 显示图例
plt.legend()

# 显示柱状图
plt.show()
