# VulnLab — SQL Injection 01

Aplicação Django **intencionalmente vulnerável**, criada exclusivamente para estudo local e autorizado.

## Regras do lab

- Rode somente em `127.0.0.1` / `localhost`.
- Não publique este projeto na internet.
- Não abra o código antes de explorar se quiser manter o efeito CTF.
- Existem **6 pontos de SQL Injection** no lab.
- Existem páginas seguras misturadas com as vulneráveis.
- Há **6 flags**.
- Pelo menos uma etapa pode exigir combinar SQL Injection com análise/cracking de hash.

## Objetivo inicial

1. Navegar pela aplicação.
2. Mapear todos os inputs controláveis.
3. Escrever suas hipóteses de onde **poderia** existir SQL Injection.
4. Só depois começar a testar.
5. Capturar as flags.
6. Quando terminar, analisar o código e criar a branch corrigida.

## Setup — Windows / Git Bash

```bash
py -m venv .venv
source .venv/Scripts/activate
py -m pip install -r requirements.txt

py manage.py migrate
py manage.py seed_lab

py manage.py runserver 127.0.0.1:8000
```

Abra:

```text
http://127.0.0.1:8000/
```

## Reset do lab

```bash
py manage.py seed_lab
```

## Branches sugeridas

```bash
git init
git add .
git commit -m "Lab 01 SQLi vulnerable"
git branch -M lab/sql-injection-01-vulnerable
```

Quando chegar a hora de corrigir:

```bash
git switch -c lab/sql-injection-01-fixed
```
