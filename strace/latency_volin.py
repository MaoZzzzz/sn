import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv


def volin():
    tips = pd.read_csv('volin-data.csv')

    sns.violinplot(x="function_name", y="latency", hue="arch", data=tips)

    # 添加标题和标签
    # plt.title("Violin Plot of Data Sets")
    plt.xlabel("Function Name")
    plt.ylabel("Latency")

    # 显示图形
    plt.show()

volin()
