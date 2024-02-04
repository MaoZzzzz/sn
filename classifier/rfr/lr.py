import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

features_file = 'merged_file.txt'
df_features = pd.read_csv(features_file)

target_file = 'merged_file_time.txt'
df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)

# 将数据分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.2, random_state=42)

# 创建线性回归模型
linear_reg_model = LinearRegression()

# 训练模型
linear_reg_model.fit(X_train, y_train)

# 进行预测
y_pred = linear_reg_model.predict(X_test)

# 计算模型的均方误差
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差（MSE）: {mse}")
