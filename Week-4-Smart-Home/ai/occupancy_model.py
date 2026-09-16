"""Train and evaluate an occupancy classifier from home sensor history."""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

FEATURES = ["temperature", "motion", "light", "sound"]
TARGET = "occupied"


def train(path="sample_sensor_data.csv"):
    df = pd.read_csv(path)
    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    return model


if __name__ == "__main__":
    train()
