import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score

features_file = 'source.txt'
df_features = pd.read_csv(features_file)

target_file = 'target.txt'
df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)

# 将数据分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.2, random_state=42)

# 创建随机森林回归模型
rf_regressor = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练模型
rf_regressor.fit(X_train, y_train.values.ravel())

# 预测测试集
y_pred = rf_regressor.predict(X_test)
#
# test = [[1119852, 7, 129.14, 9512, 10, 34485859, 0.0453902, 0, 9.81, 856.37, 14.14]]
# # 进行预测
# predicted_value = rf_regressor.predict(test)
#
# print(predicted_value)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
