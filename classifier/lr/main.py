from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score
import csv

# latency, call percent, cpu idle, io write, 每秒收包, 每秒发包
with open('../output.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    data = []

    for row in reader:
        row = [float(value) if '.' in value or 'e' in value.lower() else int(value) if value.isdigit() else value for
               value in row]

        data.append(row)

# 将数据分为特征和标签
X = [entry[:-1] for entry in data]  # 特征: 去掉最后一列
y = [entry[-1] for entry in data]  # 标签: 最后一列

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化逻辑回归模型
lr_model = LogisticRegression()

# 训练模型
lr_model.fit(X_train, y_train)

# 预测
y_pred = lr_model.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='RISCV')
recall = recall_score(y_test, y_pred, pos_label='RISCV')
f1 = f1_score(y_test, y_pred, pos_label='RISCV')
print(f"Accuracy: {accuracy}")
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
