from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_dataset(path: str | Path) -> pd.DataFrame:
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    return pd.read_csv(dataset_path)


def prepare_data(df: pd.DataFrame):
    # Columns A and B are metadata and must NOT be included as inputs
    excluded = {"A", "B"}

    # Feature columns: all columns starting with 'feature_' plus the categorical factor columns
    feature_columns = [c for c in df.columns if c.startswith("feature_")]
    categorical_cols = ["colloid_type", "starch_type", "hydrocolloid_type", "protein_type"]

    for c in categorical_cols:
        if c not in df.columns:
            raise ValueError(f"Missing categorical column: {c}")

    # Final input columns
    input_cols = [c for c in feature_columns + categorical_cols if c not in excluded]

    # Targets according to user mapping: AD -> Y1 (binary), AE -> Y2 (class), AF-AI -> Y3 (regression)
    binary_target = "AD"
    class_target = "AE"
    regression_targets = [c for c in ["AF", "AG", "AH", "AI"] if c in df.columns]

    if binary_target not in df.columns:
        raise ValueError(f"Missing binary target column '{binary_target}' (AD).")
    if class_target not in df.columns:
        raise ValueError(f"Missing class target column '{class_target}' (AE).")
    if not regression_targets:
        raise ValueError("No regression targets found. Expected AF-AI columns.")

    X = df[input_cols].astype(float).to_numpy()
    y_binary = df[binary_target].astype(float).to_numpy()
    y_class = df[class_target].astype(int).to_numpy()
    y_regression = df[regression_targets].astype(float).to_numpy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, yb_train, yb_test, yc_train, yc_test, yr_train, yr_test = train_test_split(
        X_scaled,
        y_binary,
        y_class,
        y_regression,
        test_size=0.2,
        random_state=42,
    )

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_binary_train": yb_train,
        "y_binary_test": yb_test,
        "y_class_train": yc_train,
        "y_class_test": yc_test,
        "y_regression_train": yr_train,
        "y_regression_test": yr_test,
        "feature_columns": input_cols,
        "regression_targets": regression_targets,
        "scaler": scaler,
    }
