import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

# From file
file_path = 'data.txt'  # Replace with your actual file path

# Read data from file
with open(file_path, 'r') as file:
    data_lines = file.readlines()

# Process data
data_list = [line.strip().split(',') for line in data_lines if line.strip() and len(line.strip().split(',')) == 3]
df = pd.DataFrame(data_list, columns=['Operation', 'Column1', 'Column2'])
df['Column1'] = df['Column1'].apply(lambda x: float(x.strip('<>')))
df['Column2'] = df['Column2'].apply(lambda x: float(x.strip('<>')))

# Normalize data
df['Normalized'] = df['Column2'] / df['Column1']
df['one'] = 1

# Plotting
fig, ax = plt.subplots(figsize=(18, 6))
bar_width = 0.4
opacity = 0.8

bar1 = ax.bar(df.index, df['one'], bar_width, alpha=opacity, color='b', label='X86')
bar2 = ax.bar(df.index + bar_width, df['Normalized'], bar_width, alpha=opacity, color='g', label='RISCV')

ax.set_xlabel('系统调用名称')
ax.set_ylabel('归一化结果')
ax.set_title('X86 和 RISCV 系统调用执行时间对比')

plt.xticks(df.index + bar_width / 2, df['Operation'], rotation=90)
plt.margins(x=0.01)

ax.set_xticklabels(df['Operation'])
ax.legend()

plt.tight_layout()
plt.savefig('系统调用对比.png')
plt.show()
