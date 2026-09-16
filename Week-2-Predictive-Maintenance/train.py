from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

RNG = np.random.default_rng(42)
FEATURES = ["temperature", "vibration", "pressure", "rpm", "operating_hours"]


def make_demo_data(n=1500):
    df = pd.DataFrame({
        "temperature": RNG.normal(70, 8, n),
        "vibration": RNG.normal(3.0, 0.8, n),
        "pressure": RNG.normal(100, 10, n),
        "rpm": RNG.normal(1500, 180, n),
        "operating_hours": RNG.uniform(100, 10000, n),
    })
    risk = (df.vibration > 3.7) | (df.temperature > 82) | (df.operating_hours > 8500)
    df["failure"] = risk.astype(int)
    return df


def main(csv_path=None):
    df = pd.read_csv(csv_path) if csv_path and Path(csv_path).exists() else make_demo_data()
    X = df[FEATURES].replace([np.inf, -np.inf], np.nan).fillna(df[FEATURES].median())
    y = df["failure"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print("ROC-AUC:", round(roc_auc_score(y_test, prob), 4))
    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump(model, "artifacts/predictive_maintenance_model.joblib")


if __name__ == "__main__":
    main()
