import matplotlib.pyplot as plt
from file_util import *

x_values = list(range(0, 30))
user_result_riscv, idle_result_riscv, iowait_result_riscv = read_file("cpu", "riscv")
bread_result_riscv, bwrite_result_riscv = read_file("io", "riscv")
user_result_x86, idle_result_x86, iowait_result_x86 = read_file("cpu", "x86")
bread_result_x86, bwrite_result_x86 = read_file("io", "x86")

figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# ax1 = figure.add_subplot(1, 1, 1)

ax1.plot(x_values, user_result_riscv[0:30], marker='s', linestyle='-', lw=2, c='black', label="user_riscv")
ax1.plot(x_values, idle_result_riscv[0:30], marker='o', linestyle='-', lw=2, c='brown', label="idle_riscv")
ax1.plot(x_values, iowait_result_riscv[0:30], marker='+', linestyle='-', lw=2, c='navy', label="iowite_riscv")
ax1.plot(x_values, user_result_x86[0:30], marker='^', linestyle='-', lw=2, c='chocolate', label="user_x86")
ax1.plot(x_values, idle_result_x86[0:30], marker='v', linestyle='-', lw=2, c='tan', label="idle_x86")
ax1.plot(x_values, iowait_result_x86[0:30], marker=',', linestyle='-', lw=2, c='indigo', label="iowite_x86")
ax1.legend(loc="upper right")

ax2.plot(x_values, bread_result_riscv[0:30], marker='+', linestyle='-', lw=2, c='orange', label="bread_riscv")
ax2.plot(x_values, bwrite_result_riscv[0:30], marker='*', linestyle='-', lw=2, c='gold', label="bwrite_riscv")
ax2.plot(x_values, bread_result_x86[0:30], marker=',', linestyle='-', lw=2, c='green', label="bread_x86")
ax2.plot(x_values, bwrite_result_x86[0:30], marker='x', linestyle='-', lw=2, c='pink', label="bwrite_x86")
ax2.legend(loc="upper right")

plt.xticks(x_values)

# plt.show()
plt.savefig("./picture/compose-post.jpg")
