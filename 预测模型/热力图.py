import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 绘制热力图
sns.heatmap(data, annot=True, fmt="d")

# 显示图形
plt.show()
