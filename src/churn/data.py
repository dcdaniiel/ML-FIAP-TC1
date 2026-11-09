"""Carga e limpeza do dataset (Etapa 1)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_raw(path: Path) -> pd.DataFrame:
    """Lê o CSV bruto. A limpeza específica do dataset entra aqui na Etapa 1."""
    return pd.read_csv(path)
