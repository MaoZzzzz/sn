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

    print("KNN 模型结果")
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_variance = explained_variance_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R^2 Score:", r2)
    print("Explained Variance Score:", explained_variance)

    return knn_classifier


def rfr(X_train, X_test, y_train, y_test):
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train.values.ravel())
    y_pred = rf_regressor.predict(X_test)

    print("RFR 模型结果")
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_variance = explained_variance_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R^2 Score:", r2)
    print("Explained Variance Score:", explained_variance)

    return rf_regressor


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

    print("LR 模型结果")
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_variance = explained_variance_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R^2 Score:", r2)
    print("Explained Variance Score:", explained_variance)

    return model


def svr(X_train, X_test, y_train, y_test):
    model = SVR(kernel='rbf', C=1.0, gamma='scale')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("SVR 模型结果")
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_variance = explained_variance_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R^2 Score:", r2)
    print("Explained Variance Score:", explained_variance)

    return model


def mlp(X_train, X_test, y_train, y_test):
    model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("MLP 模型结果")
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_variance = explained_variance_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R^2 Score:", r2)
    print("Explained Variance Score:", explained_variance)

    return model


def dump(model):
    joblib.dump(model, 'knn_model.joblib')


def train(features_file, target_file, model_list):
    df_features = pd.read_csv(features_file)
    df_target = pd.read_csv(target_file, header=None, names=['target'], skiprows=1)
    df = pd.concat([df_features, df_target], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["target"]), df["target"], test_size=0.2,
                                                        random_state=42)

    for model in model_list:
        if model == "0":
            rfr(X_train, X_test, y_train, y_test)
        elif model == "1":
            knn(X_train, X_test, y_train, y_test)
        elif model == "2":
            lr(features_file, target_file)
        elif model == "3":
            svr(X_train, X_test, y_train, y_test)
        elif model == "4":
            mlp(X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    model_list = ["0", "1", "2", "3", "4"]
    train("/rfaas/classifier/classifier/bake/input.txt",
          "D:\Workdir\pycharm\sn\classifier\classifier\\bake\latency.txt", model_list)
