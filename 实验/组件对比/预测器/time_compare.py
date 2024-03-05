import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from scipy.optimize import curve_fit
import numpy as np
import time

plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams.update({'font.size': 25})

time_data = []


# 定义二次函数模型
def quadratic_func(x, a, b, c):
    return a * x ** 2 + b * x + c


def data_create(i):
    x = np.random.rand(i, 10)  # 3000条数据，每条数据有10个特征
    y = np.random.randint(0, 2, i)  # 3000个随机标签

    knn = KNeighborsClassifier()
    rfr = RandomForestClassifier(n_estimators=10, random_state=42)
    svc = SVC()
    mlp = MLPClassifier()

    start_time = time.time()
    knn.fit(x, y)
    end_time = time.time()
    time_data.append(end_time - start_time)

    start_time = time.time()
    rfr.fit(x, y)
    end_time = time.time()
    time_data.append(end_time - start_time)

    start_time = time.time()
    svc.fit(x, y)
    end_time = time.time()
    time_data.append(end_time - start_time)

    start_time = time.time()
    mlp.fit(x, y)
    end_time = time.time()
    time_data.append(end_time - start_time)

    x = np.linspace(0, 10, 10000)  # 3000个数据点
    y = 2 * x ** 2 - 3 * x + 1 + np.random.normal(0, 1, 10000)  # 二次函数加上噪声
    start_time = time.time()
    params, covariance = curve_fit(quadratic_func, x, y)
    end_time = time.time()
    time_data.append(end_time - start_time)

    print(time_data)


if __name__ == '__main__':
   data_create(30000)