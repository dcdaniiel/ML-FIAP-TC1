"""API de inferência (FastAPI). Endpoints obrigatórios: /health e /predict."""

from __future__ import annotations

from fastapi import FastAPI

from churn import __version__

app = FastAPI(
    title="Churn Prediction API",
    version=__version__,
    description="Tech Challenge Fase 1 - propensão de churn de clientes de telecom.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Verifica se a API está no ar."""
    return {"status": "ok", "version": __version__}


def run() -> None:
    """Entry point `churn-api`: sobe o servidor local."""
    import uvicorn

    uvicorn.run("churn.api.main:app", host="0.0.0.0", port=8000, reload=True)
