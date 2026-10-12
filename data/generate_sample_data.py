import pandas as pd
import numpy as np
from pathlib import Path


def generate_dataset(path: Path, n_samples: int = 400):
    rng = np.random.default_rng(42)
    n_features = 10

    # Columns A and B are metadata and should NOT be used as inputs
    col_A = rng.integers(1000, 9999, size=n_samples)  # sample ID or similar
    col_B = rng.choice(["note1", "note2", "note3"], size=n_samples)

    # Continuous experimental features
    X = rng.normal(0, 1, size=(n_samples, n_features))
    feature_columns = [f"feature_{i + 1}" for i in range(n_features)]

    # Categorical factors encoded according to user mapping
    # Colloid type: CaCl2=1, NaCl=2, urea=3
    colloid_type = rng.integers(1, 4, size=n_samples)

    # Starch type codes 1..18 (see README for mapping)
    starch_type = rng.integers(1, 19, size=n_samples)

    # Hydrocolloid type codes 1..11
    hydrocolloid_type = rng.integers(1, 12, size=n_samples)

    # Protein type codes 1..11
    protein_type = rng.integers(1, 12, size=n_samples)

    # Define outputs based on a simple synthetic model
    # AD (Y1): binary printability flag (0/1)
    score_y1 = 0.6 * X[:, 0] - 0.4 * X[:, 1] + 0.2 * (colloid_type == 1) + rng.normal(0, 0.3, size=n_samples)
    AD = (score_y1 > 0.0).astype(int)

    # AE (Y2): categorical printability class {0,1,2}
    score_y2 = 0.5 * X[:, 2] + 0.3 * X[:, 3] - 0.2 * (starch_type > 10) + rng.normal(0, 0.35, size=n_samples)
    AE = np.where(score_y2 > 0.6, 2, np.where(score_y2 > -0.1, 1, 0))

    # AF-AI (Y3): four texture-related continuous properties
    AF = 1.0 + 0.4 * X[:, 0] - 0.2 * X[:, 4] + 0.1 * (hydrocolloid_type == 1) + rng.normal(0, 0.08, size=n_samples)
    AG = 0.9 + 0.3 * X[:, 1] + 0.2 * X[:, 5] + 0.05 * (protein_type == 4) + rng.normal(0, 0.1, size=n_samples)
    AH = 1.1 + 0.25 * X[:, 2] - 0.15 * X[:, 6] + rng.normal(0, 0.12, size=n_samples)
    AI = 0.7 + 0.35 * X[:, 3] + 0.22 * X[:, 7] + rng.normal(0, 0.1, size=n_samples)

    df = pd.DataFrame(X, columns=feature_columns)
    df.insert(0, "B", col_B)
    df.insert(0, "A", col_A)

    # Append categorical factor columns
    df["colloid_type"] = colloid_type
    df["starch_type"] = starch_type
    df["hydrocolloid_type"] = hydrocolloid_type
    df["protein_type"] = protein_type

    # Map outputs to Excel-like column names AD, AE, AF..AI
    df["AD"] = AD
    df["AE"] = AE
    df["AF"] = AF
    df["AG"] = AG
    df["AH"] = AH
    df["AI"] = AI

    output_dir = path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved synthetic dataset to {path}")


if __name__ == "__main__":
    generate_dataset(Path("data/synthetic_printability_data.csv"))
