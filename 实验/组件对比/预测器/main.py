import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

data = np.loadtxt('D:\Workdir\pycharm\sn\实验\组件对比\调度器\compose-post-rfr.txt')

plt.boxplot(data)

plt.show()
