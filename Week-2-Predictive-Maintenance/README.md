# Week 2 — Predictive Maintenance

A practical machine-learning pipeline for predicting whether an industrial machine is approaching failure.

## Pipeline
1. Load sensor telemetry (temperature, vibration, pressure, RPM, operating hours).
2. Validate and clean missing/outlier values.
3. Create rolling/statistical features.
4. Split data into train/test sets without leakage.
5. Train a classifier such as Random Forest.
6. Evaluate precision, recall, F1, confusion matrix, and ROC-AUC.
7. Export the trained model for an edge or server application.

## Run
```bash
pip install -r requirements.txt
python train.py
```

The example script generates a reproducible synthetic dataset when no CSV is supplied, so the project can be tested without proprietary industrial data.
