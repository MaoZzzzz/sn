import matplotlib.pyplot as plt
import numpy as np

figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

categories = ['mprotect', 'write', 'fstat', 'set_robust_list', 'brk', 'close', 'lseek', 'gettid', 'getrandom', 'munmap',
              'clone', 'read', 'prlimit64', 'mmap', 'wait4', 'getsockname', 'getpid', 'ioctl', 'openat', 'stat',
              'newfstatat', 'pipe2', 'exit_group', 'socketpair']
x86_value = [0.000385, 0.08296699999999999, 0.14261299999999993, 0.049337, 0.004209999999999999, 0.319297,
             0.13149600000000003, 0.079911, 0.043529999999999985, 0.000225, 0.189254, 0.10924, 0.00015, 0.002809,
             0.153616, 0.024054, 0.148404, 0.170254, 0.101661, 0.2160829999999999, 0.0, 0.113035, 0.0, 0.012705]
riscv_value = [0.000291, 0.05247400000000001, 0.0, 0.046952000000000015, 4.8e-05, 0.25172100000000003,
               0.045926000000000015, 0.049590999999999996, 0.09068399999999997, 0.000167, 0.381682, 0.051422, 4.2e-05,
               0.000864, 0.103122, 0.010701, 0.09522, 0.061225999999999996, 0.06408499999999999, 0.0,
               0.04853699999999998, 0.068513, 0.0, 0.010723]

# 0.024167  0.631387
bar_width = 0.35

index = np.arange(len(categories))

plt.subplot(2, 1, 1)
plt.bar(index, x86_value, bar_width, label='Time Point 1', color='#7B3100')
plt.bar(index + bar_width, riscv_value, bar_width, label='Time Point 2', color='#A06C4F')
plt.title('')
plt.xlabel('system call name')
plt.ylabel('time(s)')

plt.xticks(index + bar_width / 2, categories, rotation=45)

plt.legend()

categories_select = ["select"]
x86_select = [0.099108]
riscv_select = [0.631387]

index = np.arange(len(categories_select))
plt.subplot(2, 1, 2)
plt.bar(index, x86_select, bar_width, label='Time Point 1', color='#7B3100')
plt.bar(index + bar_width, riscv_select, bar_width, label='Time Point 2', color='#A06C4F')
plt.title('')
plt.xlabel('system call name')
plt.ylabel('time(s)')

plt.xticks(index + bar_width / 2, categories_select)

plt.legend()
plt.tight_layout()

plt.show()
