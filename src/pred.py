import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_and_predict(data, features, target, test_size=0.2, random_state=42):
    """
    Train a Random Forest model and make predictions.

    Parameters:
        data (pd.DataFrame): The dataset containing features and target.
        features (list): List of column names to use as features.
        target (str): The target column name.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.

    Returns:
        dict: A dictionary containing the model, predictions, and evaluation metrics.
    """
    # Split the data into training and testing sets
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train the Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return {
        "model": model,
        "predictions": y_pred,
        "mse": mse,
        "r2": r2,
        "X_test": X_test,
        "y_test": y_test
    }