# ML-FIAP-TC1 - Pipeline Preditivo de Churn

Tech Challenge da Fase 1 da Pós Tech em Machine Learning Engineering (FIAP, turma 13MLET).

Uma operadora de telecomunicações está perdendo clientes. O objetivo é construir, da análise exploratória ao modelo servido via API, um classificador de propensão a churn usando o ecossistema Scikit-Learn (regressão logística, árvores/ensembles e MLP) e expô-lo com FastAPI.

## Estrutura

```
.
├── data/
│   ├── raw/            # dataset bruto (não versionado)
│   └── processed/      # dados tratados (não versionado)
├── docs/               # ML Canvas, Model Card e demais documentos
├── models/             # artefatos .joblib (não versionados)
├── notebooks/          # experimentação (EDA, baselines, comparação)
├── src/churn/          # código produtivo
│   ├── config.py       # caminhos, seed e constantes
│   ├── data.py         # carga e limpeza
│   ├── features.py     # pré-processamento
│   ├── train.py        # treino e comparação de modelos
│   ├── predict.py      # inferência com o modelo campeão
│   └── api/main.py     # FastAPI (/health, /predict)
└── tests/              # pytest
```

Notebooks são para experimentação; tudo que vai para produção vive em `src/churn/` como módulo `.py`.

## Setup

Requisitos: Python 3.12 e [uv](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
```

Para os notebooks:

```bash
uv sync --extra dev --extra notebooks
```

Variáveis de ambiente opcionais estão em `.env.example`.

## Execução

Rodar a API localmente:

```bash
uv run churn-api
```

A documentação interativa fica em http://localhost:8000/docs.

Rodar os testes:

```bash
uv run pytest
```

Lint:

```bash
uv run ruff check .
```

## Dataset

Sugerido: [Telco Customer Churn (IBM, Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). Baixe o CSV para `data/raw/`.

## Etapas

| Etapa | Foco                                                                    | Entregável                           |
| ----- | ----------------------------------------------------------------------- | ------------------------------------ |
| 1     | Entendimento e preparação: ML Canvas, EDA, métricas, baseline logístico | Notebook de EDA + baseline           |
| 2     | Modelagem: Random Forest, MLPClassifier, validação cruzada, comparação  | Tabela comparativa + modelo salvo    |
| 3     | Engenharia: refatoração para `src/`, pytest, API FastAPI                | Repositório refatorado + API testada |
| 4     | Documentação: Model Card, README final, vídeo STAR                      | Repositório final + vídeo            |

## Convenção de commits

Commits atômicos e mensagens no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/):
`<tipo>[escopo]: <descrição>` no imperativo, sem ponto final, até 50 caracteres. Regras, exemplos e fluxo em [CONTRIBUTING.md](CONTRIBUTING.md).

Ative o template e a validação local uma vez após clonar:

```bash
git config core.hooksPath .githooks
git config commit.template .gitmessage
```

## Reprodutibilidade

Seed global fixada em `churn.config.SEED` (42). Use `set_seed()` antes de qualquer treino.

## Documentação

- [ML Canvas](docs/ml_canvas.md)
- [Model Card](docs/model_card.md)
