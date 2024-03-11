from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import pandas as pd
import joblib


def knn(X_train, X_test, y_train, y_test):
    knn_classifier = KNeighborsRegressor(n_neighbors=5)
    knn_classifier.fit(X_train, y_train.values.ravel())
    y_pred = knn_classifier.predict(X_test)

    prediction_error_rate = ((y_pred - y_test.values.ravel()) / y_test.values.ravel()) * 100

    return y_pred


def rfr(X_train, X_test, y_train, y_test):
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train.values.ravel())
    y_pred = rf_regressor.predict(X_test)

    prediction_error_rate = ((y_pred - y_test.values.ravel()) / y_test.values.ravel()) * 100

    return y_pred
    # print("RFR 模型结果")
    # mse = mean_squared_error(y_test, y_pred)
    # mae = mean_absolute_error(y_test, y_pred)
    # r2 = r2_score(y_test, y_pred)
    # explained_variance = explained_variance_score(y_test, y_pred)
    #
    # print("Mean Squared Error:", mse)
    # print("Mean Absolute Error:", mae)
    # print("R^2 Score:", r2)
    # print("Explained Variance Score:", explained_variance)

    # return rf_regressor


def lr(features_file, target_file):
    df_features = pd.read_csv(features_file)
    df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)

    X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.2, random_state=42)
    y_train = y_train.values.ravel()

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    prediction_error_rate = ((y_pred - y_test.values.ravel()) / y_test.values.ravel()) * 100

    return y_pred


def svr(X_train, X_test, y_train, y_test):
    model = SVR(kernel='rbf', C=1.0, gamma='scale')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    prediction_error_rate = ((y_pred - y_test.values.ravel()) / y_test.values.ravel()) * 100

    return y_pred


def mlp(X_train, X_test, y_train, y_test):
    model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    prediction_error_rate = ((y_pred - y_test.values.ravel()) / y_test.values.ravel()) * 100

    return y_pred


def train(features_file, target_file, model_list, output_file):
    df_features = pd.read_csv(features_file)
    df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)
    df = pd.concat([df_features, df_target], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["target"]), df["target"], test_size=0.2,
                                                        random_state=42)

    for model in model_list:
        if model == "0":
            with open(output_file + "{}_predict_time.txt".format("rfr"), 'a') as f:
                for i, error_rate in enumerate(rfr(X_train, X_test, y_train, y_test)):
                    f.write(str(error_rate) + "\n")
        elif model == "1":
            with open(output_file + "{}_predict_time.txt".format("knn"), 'a') as f:
                for i, error_rate in enumerate(knn(X_train, X_test, y_train, y_test)):
                    f.write(str(error_rate) + "\n")
        elif model == "2":
            with open(output_file + "{}_predict_time.txt".format("lr"), 'a') as f:
                for i, error_rate in enumerate(lr(features_file, target_file)):
                    f.write(str(error_rate) + "\n")
        elif model == "3":
            with open(output_file + "{}_predict_time.txt".format("svr"), 'a') as f:
                for i, error_rate in enumerate(svr(X_train, X_test, y_train, y_test)):
                    f.write(str(error_rate) + "\n")
        elif model == "4":
            with open(output_file + "{}_predict_time.txt".format("mlp"), 'a') as f:
                for i, error_rate in enumerate(mlp(X_train, X_test, y_train, y_test)):
                    f.write(str(error_rate) + "\n")


if __name__ == '__main__':
    functionNames = ["compose_post", "upload_creator", "upload_text", "upload_media", "upload_unique_id",
                     "upload_user_mentions", "post_storage", "upload_home_timeline",
                     "upload_user_timeline", "matmul"]
    for functionName in functionNames:
        model_list = ["0", "1", "2", "3", "4"]

        source_path = "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\{}_source.txt".format(
            functionName)
        target_path = "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\{}_target.txt".format(
            functionName)
        output_file = "D:\Workdir\pycharm\sn\\rfaas\classifier\classifier\stage2\\riscv\\time_result\\"
        train(source_path, target_path, model_list, output_file)
