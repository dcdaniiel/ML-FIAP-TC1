"""Configuração central: caminhos, seed e constantes do projeto."""

from __future__ import annotations

import os
import random
from pathlib import Path

import numpy as np

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT_DIR / "models"

SEED = int(os.getenv("CHURN_SEED", "42"))
MODEL_PATH = ROOT_DIR / os.getenv("CHURN_MODEL_PATH", "models/model.joblib")

TARGET = "Churn"


def set_seed(seed: int = SEED) -> None:
    """Fixa as seeds de random e numpy para reprodutibilidade."""
    random.seed(seed)
    np.random.seed(seed)
