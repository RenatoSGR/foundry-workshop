# Lab 04 — Workflows com LLM

Guia passo a passo para criar **pipelines de chamadas encadeadas** ao modelo (prompt chaining) no Foundry v2.

---

## Passo 1 — Compreender Workflows LLM

Um **Workflow LLM** é um pipeline onde cada passo usa o modelo para uma tarefa específica:
- **Passo 1**: Analisar o input (ex: extrair entidades)
- **Passo 2**: Processar (ex: classificar, traduzir)
- **Passo 3**: Gerar output final (ex: resumo estruturado)

Cada passo recebe o output do anterior como contexto.

---

## Passo 2 — Testar Prompt Chaining no Playground

1. No portal Foundry → **Playgrounds** → **Chat**
2. Testa cada passo individualmente:
   - Envia um texto e pede ao modelo para **extrair entidades**
   - Copia o resultado e pede para **classificar**
   - Copia e pede para **gerar um resumo**
3. Observa como cada passo transforma a informação

---

## Passo 3 — Automatizar via Código

1. Abre o notebook [`lab04-model-workflows.ipynb`](lab04-model-workflows.ipynb)
2. Executa as células por ordem — o notebook demonstra:
   - Encadear múltiplas chamadas ao modelo
   - Passar o output de uma chamada como input da seguinte
   - Construir pipelines de processamento de texto

---

## Passo 4 — Explorar no Portal (Prompt Flow)

1. No portal Foundry → **Build** → **Prompt flow**
2. Cria um novo flow a partir de um template ou em branco
3. Adiciona nós de **LLM** encadeados
4. Liga os outputs de um nó aos inputs do seguinte
5. Testa o flow completo no playground integrado

---

## Resultado Esperado

- Pipeline funcional com múltiplas chamadas encadeadas ao modelo
- Compreensão de como orquestrar prompt chaining via código e via portal
