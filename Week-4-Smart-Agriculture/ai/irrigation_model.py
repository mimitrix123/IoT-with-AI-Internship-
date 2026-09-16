"""Small AI-assisted irrigation recommendation module.

Train on historical sensor rows with columns:
soil_raw, temperature, light, irrigation_needed
"""
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

DATA = Path(__file__).with_name("sample_sensor_data.csv")


def train(csv_path=DATA):
    df = pd.read_csv(csv_path)
    X = df[["soil_raw", "temperature", "light"]]
    y = df["irrigation_needed"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test)))
    return model


if __name__ == "__main__":
    train()
