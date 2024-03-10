import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

features_file = 'bake/source.txt'
features_file = 'bake/source_wo_system_call.txt'
df_features = pd.read_csv(features_file)

target_file = 'bake/target.txt'
df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)

# 将数据分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.2, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 创建 MLP 模型
model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', random_state=42)

# 在训练集上训练模型
model.fit(X_train_scaled, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print("精确度:", precision)
print("召回率:", recall)
print("F1 分数:", f1)
print("准确率:", accuracy)

