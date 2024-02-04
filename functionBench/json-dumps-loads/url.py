import matplotlib.pyplot as plt
from file_util import *

x_values = list(range(0, 10))
iseg_result_riscv, oseg_result_riscv = read_file("net", "riscv")
iseg_result_x86, oseg_result_x86 = read_file("net", "x86")

figure, ax1 = plt.subplots(1, 1, figsize=(12, 6), sharex=True)

# ax1 = figure.add_subplot(1, 1, 1)

ax1.plot(x_values, iseg_result_riscv[0:10], marker='s', linestyle='-', lw=2, c='black', label="iseg_riscv")
ax1.plot(x_values, oseg_result_riscv[0:10], marker='o', linestyle='-', lw=2, c='brown', label="oseg_riscv")
ax1.plot(x_values, iseg_result_x86[0:10], marker='+', linestyle='-', lw=2, c='navy', label="iseg_x86")
ax1.plot(x_values, oseg_result_x86[0:10], marker='^', linestyle='-', lw=2, c='chocolate', label="oseg_x86")
ax1.legend(loc="upper right")

plt.xticks(x_values)

# plt.show()
plt.savefig("./picture/json-dumps-loads.jpg")
