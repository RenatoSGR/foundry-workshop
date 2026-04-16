# Lab 02 — Agentes no Microsoft Foundry

Guia passo a passo para criar agentes com **tools** e com o **Agent Service** no Foundry.

> 📖 **Referência oficial:** [What is Microsoft Foundry Agent Service?](https://learn.microsoft.com/azure/foundry/agents/overview)

---

## Parte A — Agentes com a Responses API (lab02)

### Passo 1 — Compreender o Conceito de Agente

Um **Agente** no Foundry é um assistente que pode:
- Usar **ferramentas** (code interpreter, file search, web search, functions)
- Manter contexto ao longo de uma conversa
- Executar ações autonomamente com base em instruções

O Foundry suporta três tipos de agentes:
- **Prompt agents** — configurados via portal, sem código
- **Workflow agents** (preview) — orquestração multi-agente visual
- **Hosted agents** (preview) — containers com código personalizado

### Passo 2 — Criar um Agente via Código

1. Abre o notebook [`lab02-agentes.ipynb`](lab02-agentes.ipynb)
2. Executa as células por ordem — o notebook demonstra:
   - Criar um agente com a **Responses API** do Azure OpenAI
   - Definir **tools** (funções) que o agente pode chamar
   - Processar **function calling** — o modelo decide quando usar cada ferramenta

### Passo 3 — Testar no Portal (Model Playground)

1. No portal Foundry → **Build** → **Models** → seleciona o deployment `gpt-4o`
2. No Playground, expande a secção **Tools** e adiciona **Code interpreter** ou uma função personalizada
3. Envia uma mensagem que exija o uso da ferramenta e observa o fluxo

---

## Parte B — Agentes com o Agent Service (lab02.1)

### Passo 1 — Criar um Prompt Agent no Portal

1. No portal Foundry → **Build** → **Agents**
2. Clica em **+ New agent** → escolhe **Prompt agent**
3. Configura:
   - **Nome**: ex. `assistente-workshop`
   - **Instructions**: define o comportamento do agente
   - **Model**: seleciona `gpt-4o`
4. O agente é criado automaticamente

> ⚠️ **Nota:** Depois de dares nome ao agente, não podes alterá-lo. Em código, referes o agente como `<agent_name>:<version>`.

### Passo 2 — Adicionar Tools ao Agente

1. Na configuração do agente, secção **Tools**
2. Adiciona ferramentas disponíveis (Code Interpreter, File Search, Web Search)
3. Para mais ferramentas, vai a **Build** → **Tools** para explorar o catálogo de ferramentas (incluindo MCP servers)
4. Guarda as alterações

### Passo 3 — Testar no Agents Playground

1. O **Agents Playground** abre integrado no painel do agente
2. Envia mensagens e observa o agente a usar as ferramentas
3. No separador **Code**, podes copiar o código ou abrir diretamente no **VS Code for the Web**

### Passo 4 — Consumir via Código

1. Abre o notebook [`lab02.1-agentes.ipynb`](lab02.1-agentes.ipynb)
2. Executa as células — o notebook demonstra:
   - Criar um agente com `AIProjectClient`
   - Ciclo **Agent → Conversation → Response**
   - O agente fica visível no portal do Foundry

---

## Resultado Esperado

- Agente criado e funcional com tools (function calling)
- Agente visível e testável no portal do Foundry
