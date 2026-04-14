# Lab 05 — Multi-Agent Workflows

Guia passo a passo para criar **workflows multi-agente** com o Foundry Agent Service.

---

## Passo 1 — Compreender Multi-Agent Workflows

No Foundry, podes criar **workflows multi-agente server-side** onde:
- Vários agentes especializados colaboram numa tarefa
- Um **orquestrador** delega sub-tarefas a agentes conectados
- Os agentes comunicam via **Connected Agents** (ConnectedAgentTool)

---

## Passo 2 — Criar os Agentes Especializados no Portal

1. No portal Foundry → **Build** → **Agents**
2. Cria **2-3 agentes** especializados, cada um com instruções específicas:
   - Ex: `agente-pesquisa` — especializado em pesquisa
   - Ex: `agente-analise` — especializado em análise de dados
   - Ex: `agente-redacao` — especializado em redigir respostas
3. Para cada agente, define as **instructions** e o **modelo**

---

## Passo 3 — Criar o Agente Orquestrador

1. Cria um novo agente: `orquestrador`
2. Nas **Tools**, adiciona **Connected Agents**:
   - Seleciona os agentes criados no Passo 2
   - Define quando cada agente deve ser invocado
3. Nas **Instructions**, explica ao orquestrador como delegar tarefas

---

## Passo 4 — Testar no Playground

1. Abre o **Playground** do agente orquestrador
2. Envia uma mensagem que exija colaboração entre agentes
3. Observa o orquestrador a delegar e a compilar as respostas

---

## Passo 5 — Implementar via Código

1. Abre o notebook [`lab05b-agent-workflows.ipynb`](lab05b-agent-workflows.ipynb)
2. Executa as células — o notebook demonstra:
   - Criar agentes via `AIProjectClient`
   - Ligar agentes com `ConnectedAgentTool`
   - Orquestrar o workflow multi-agente programaticamente

---

## Resultado Esperado

- Workflow multi-agente funcional com orquestrador e agentes especializados
- Agentes visíveis e conectados no portal do Foundry
