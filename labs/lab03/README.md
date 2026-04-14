# Lab 03 — Agentes no Microsoft Foundry

Guia passo a passo para criar agentes com **tools** e com o **Agent Service** no Foundry v2.

---

## Parte A — Agentes com a Responses API (lab03)

### Passo 1 — Compreender o Conceito de Agente

Um **Agente** no Foundry é um assistente que pode:
- Usar **ferramentas** (code interpreter, file search, functions)
- Manter contexto ao longo de uma conversa
- Executar ações autonomamente com base em instruções

### Passo 2 — Criar um Agente via Código

1. Abre o notebook [`lab03-agentes.ipynb`](lab03-agentes.ipynb)
2. Executa as células por ordem — o notebook demonstra:
   - Criar um agente com a **Responses API** do Azure OpenAI
   - Definir **tools** (funções) que o agente pode chamar
   - Processar **function calling** — o modelo decide quando usar cada ferramenta

### Passo 3 — Testar no Portal (Playground)

1. No portal Foundry → **Playgrounds** → **Chat**
2. Ativa **Tools** e adiciona uma função personalizada
3. Envia uma mensagem que exija o uso da ferramenta e observa o fluxo

---

## Parte B — Agentes com o Agent Service (lab03.1)

### Passo 1 — Criar um Agente no Portal

1. No portal Foundry → **Build** → **Agents**
2. Clica em **+ New agent**
3. Configura:
   - **Nome**: ex. `assistente-workshop`
   - **Instructions**: define o comportamento do agente
   - **Model**: seleciona `gpt-4o`
4. Clica **Create**

### Passo 2 — Adicionar Tools ao Agente

1. Na configuração do agente, secção **Tools**
2. Adiciona ferramentas disponíveis (Code Interpreter, File Search, Functions)
3. Guarda as alterações

### Passo 3 — Testar no Playground do Agente

1. Usa o **Playground** integrado no painel do agente
2. Envia mensagens e observa o agente a usar as ferramentas

### Passo 4 — Consumir via Código

1. Abre o notebook [`lab03.1-agentes.ipynb`](lab03.1-agentes.ipynb)
2. Executa as células — o notebook demonstra:
   - Criar um agente standard com `AIProjectClient`
   - Ciclo **Agent → Conversation → Response**
   - O agente fica visível no portal do Foundry

---

## Resultado Esperado

- Agente criado e funcional com tools (function calling)
- Agente visível e testável no portal do Foundry
