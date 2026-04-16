# Lab 04 — Multi-Agent Workflows

Guia passo a passo para criar **workflows multi-agente** com o Foundry Agent Service.

> 📖 **Referência oficial:** [Build a workflow in Microsoft Foundry](https://learn.microsoft.com/azure/foundry/agents/concepts/workflow)

---

## Passo 1 — Compreender Multi-Agent Workflows

No Foundry, podes criar **workflows multi-agente** de duas formas:

1. **Workflow Agents (portal)** — orquestração visual com padrões Sequential, Group Chat, ou Human-in-the-Loop
2. **Connected Agents (código)** — via `ConnectedAgentTool` no SDK Python, onde um agente principal delega a sub-agentes

---

## Passo 2 — Criar os Agentes Especializados no Portal

1. No portal Foundry → **Build** → **Agents**
2. Cria **2-3 prompt agents** especializados, cada um com instruções específicas:
   - Ex: `agente-pesquisa` — especializado em pesquisa
   - Ex: `agente-analise` — especializado em análise de dados
   - Ex: `agente-redacao` — especializado em redigir respostas
3. Para cada agente, define as **Instructions** e o **Model** (`gpt-4o`)

---

## Passo 3 — Criar um Workflow Multi-Agente no Portal

1. No portal Foundry → **Build** → **Create new workflow**
2. Escolhe o padrão **Sequential** (ou **Group chat** para colaboração dinâmica)
3. Adiciona os agentes criados no Passo 2 como nós do workflow:
   - Clica no **+** → **Invoke agent** → seleciona um agente existente
   - Repete para cada agente
4. Configura a ordem de execução e os inputs/outputs
5. Clica **Save**

---

## Passo 4 — Testar o Workflow

1. No editor do workflow, clica em **Run Workflow**
2. Envia uma mensagem que exija colaboração entre os agentes
3. Observa cada nó a executar no visualizador
4. Verifica as respostas na janela de chat

---

## Passo 5 — Implementar via Código

1. Abre o notebook [`lab04b-agent-workflows.ipynb`](lab04b-agent-workflows.ipynb)
2. Executa as células — o notebook demonstra:
   - Criar agentes via `AIProjectClient`
   - Ligar agentes com `ConnectedAgentTool`
   - Orquestrar o workflow multi-agente programaticamente

---

## Resultado Esperado

- Workflow multi-agente funcional com agentes especializados
- Agentes visíveis e conectados no portal do Foundry
