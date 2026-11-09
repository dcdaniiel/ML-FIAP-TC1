# Guia de contribuição

Regras de versionamento do projeto. O histórico de commits é critério de avaliação
("histórico limpo e significativo evidenciando o trabalho em grupo"), então vale seguir.

## Commits atômicos

Um commit = uma mudança lógica, completa e que deixa o projeto funcionando.

- Não misture assuntos (ex.: ajuste no pré-processamento + mudança na API) no mesmo commit.
- Não quebre uma mudança lógica em vários commits que, sozinhos, não fazem sentido.
- Use `git add -p` para separar trechos de um mesmo arquivo em commits diferentes.
- Testes que acompanham a mudança entram no mesmo commit; testes isolados usam `test`.
- Pergunte-se: "consigo descrever este commit em uma linha, sem usar 'e'?" Se não, divida.

## Formato da mensagem (Conventional Commits)

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos

| Tipo | Quando usar |
|---|---|
| `feat` | nova funcionalidade (novo modelo, novo endpoint, nova feature de dados) |
| `fix` | correção de bug |
| `docs` | apenas documentação (README, Model Card, ML Canvas, docstrings) |
| `style` | formatação sem mudança de comportamento (ruff format, espaços) |
| `refactor` | mudança de código que não corrige bug nem adiciona funcionalidade |
| `test` | adição ou correção de testes |
| `chore` | build, dependências, configuração, tarefas de manutenção |
| `perf` | melhoria de desempenho |
| `ci` | pipelines e automações |

### Escopos sugeridos

`data`, `features`, `train`, `predict`, `api`, `tests`, `notebooks`, `docs`, `deps`, `config`.
O escopo é opcional; use quando ajuda a localizar a mudança.

### Regras do título

1. **Modo imperativo.** Complete mentalmente: "se eu aplicar este commit, ele vai...".
   `fix(api): corrige validação do payload` (vai corrigir). Nunca `corrigido`, `correção`.
2. **Até 50 caracteres**, limite rígido de 72.
3. **Sem ponto final.**
4. **Descrição em minúscula** após os dois-pontos.
5. **Linha em branco** entre título e corpo.

### Corpo e rodapé

- O corpo explica o **porquê** e o contexto da decisão, não o óbvio do diff.
  Quebre as linhas em 72 colunas.
- O rodapé carrega metadados: `BREAKING CHANGE: ...`, `Refs #12`, `Co-authored-by: Nome <email>`.
  Em trabalho em par, use `Co-authored-by` para registrar a autoria conjunta.

### Exemplos

```
feat(train): adiciona MLPClassifier à comparação de modelos

Fecha o trio exigido pelo desafio (linear, árvore, rede neural). A
arquitetura usa uma camada oculta de 64 neurônios porque, com ~7k
linhas, redes maiores superajustaram na validação cruzada.
```

```
fix(features): trata TotalCharges vazio em clientes novos

Onze registros vêm com espaço em branco e quebravam a conversão para
float. Passam a ser imputados como zero, já que são clientes com
tenure = 0.
```

```
docs: preenche métricas do Model Card
```

```
chore(deps): fixa scikit-learn em 1.9
```

Inválidos: `Corrigido bug na API.`, `ajustes`, `feat: Adiciona Teste`, `fix api`.

## Fluxo

1. Crie um branch por tarefa: `feat/eda-baseline`, `fix/api-schema`.
2. Commits pequenos e frequentes seguindo o padrão acima.
3. Antes de abrir o PR: `uv run ruff check . && uv run pytest`.
4. PR revisado por pelo menos uma pessoa do grupo antes do merge em `main`.

## Ativando as verificações locais

O hook `commit-msg` e o template ficam versionados em `.githooks/` e `.gitmessage`.
Cada pessoa ativa uma única vez no seu clone:

```bash
git config core.hooksPath .githooks
git config commit.template .gitmessage
```

Depois disso, `git commit` (sem `-m`) abre o editor já com o guia e mensagens fora do
padrão são rejeitadas antes de entrar no histórico.
