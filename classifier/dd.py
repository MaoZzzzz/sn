import random
import csv


def modify_data(data, ratios):
    modified_data = []
    for i in range(len(data)):
        modified_row = []
        for j in range(len(data[i])):
            if isinstance(data[i][j], (int, float)):
                ratio = random.uniform(-ratios[j], ratios[j])
                modified_value = data[i][j] + data[i][j] * ratio
                modified_row.append(modified_value)
            else:
                modified_row.append(data[i][j])
        modified_data.append(modified_row)
    return modified_data


# latency, call percent, cpu idle, io write, 每秒收包, 每秒发包
format_data = [
    [0.000094392299, 0, 86.00, 553.33, 417.50, 583.83, "X86"],
    [0.004816651344, 60, 68.40, 1376.89, 1371.22, 1260.89, "RISCV"],
    [0.004058515071, 68, 68.34, 1402.00, 1314.76, 1205.99, "RISCV"],
    [0.000100575447, 0, 45.08, 1082.10, 272.36, 380.96, "X86"],
    [0.000130791187, 0, 62.09, 1681.33, 417.17, 583.33, "X86"],
    [0.000100461483, 0, 65.01, 1552.00, 501.00, 700.60, "X86"],
    [0.000177340984, 0, 65.24, 1656.00, 499.80, 699.60, "X86"],
    [0.015103614332, 67, 64.45, 6407.49, 519.86, 521.74, "RISCV"],
    [0.024893628120, 75, 64.11, 5425.81, 582.23, 540.20, "RISCV"],
    [0.011684287548, 39, 64.34, 1251.36, 891.34, 857.66, "RISCV"],
    [298.32, 0, 9.81, 856.37, 14.14, 19.33, "X86"],
]

# Ratios for modification
ratios = [0.3, 0.04, 0.07, 0.01, 0.01, 0.01]

# Modify data 100 times
for _ in range(10):
    modified_data = modify_data(format_data, ratios)
    random.shuffle(modified_data)

    with open("output.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(modified_data)
