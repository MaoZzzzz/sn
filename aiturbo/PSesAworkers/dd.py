import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()
ax1 = figure.add_subplot(1, 2, 1)
ax2 = figure.add_subplot(1, 2, 2)


ax1.plot(random(1000).cumsum())  # 绘制图形
ax2.plot(randn(180).cumsum())  # 绘制图形 返回沿给定轴的元素的累加和
ticks = ax1.set_xticks([0, 250, 500, 750, 1000])  # 设置刻度
labels = ax1.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')  # 设置刻度标签
ax1.set_title('plot1')  # 绘制标题
ax2.set_title('plot2')  # 绘制标题
ax1.set_xlabel('digital')  # 图例1
ax2.set_xlabel('digita2')
