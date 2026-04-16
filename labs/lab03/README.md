# Lab 03 — Workflows com LLM

Guia passo a passo para criar **pipelines de chamadas encadeadas** ao modelo (prompt chaining) no Foundry.

> 📖 **Referência oficial:** [Microsoft Foundry Playgrounds](https://learn.microsoft.com/azure/foundry/concepts/concept-playgrounds)

---

## Passo 1 — Compreender Workflows LLM

Um **Workflow LLM** é um pipeline onde cada passo usa o modelo para uma tarefa específica:
- **Passo 1**: Analisar o input (ex: extrair entidades)
- **Passo 2**: Processar (ex: classificar, traduzir)
- **Passo 3**: Gerar output final (ex: resumo estruturado)

Cada passo recebe o output do anterior como contexto.

---

## Passo 2 — Testar Prompt Chaining no Playground

1. No portal Foundry → **Build** → **Models** → seleciona o deployment `gpt-4o`
2. No Playground, testa cada passo individualmente:
   - Envia um texto e pede ao modelo para **extrair entidades**
   - Copia o resultado e pede para **classificar**
   - Copia e pede para **gerar um resumo**
3. Observa como cada passo transforma a informação

> 💡 **Dica:** Podes usar o **Compare mode** (botão no canto superior direito do Playground) para testar o mesmo prompt em até 3 modelos em simultâneo.

---

## Passo 3 — Automatizar via Código

1. Abre o notebook [`lab03-model-workflows.ipynb`](lab03-model-workflows.ipynb)
2. Executa as células por ordem — o notebook demonstra:
   - Encadear múltiplas chamadas ao modelo
   - Passar o output de uma chamada como input da seguinte
   - Construir pipelines de processamento de texto

---

## Passo 4 — Explorar Workflows no Portal

No Foundry, podes criar **Workflow Agents** que orquestram ações visualmente:

1. No portal Foundry → **Build** → clica em **Create new workflow**
2. Escolhe um template (ex: **Sequential**) ou cria em branco
3. Adiciona nós de **Invoke agent** encadeados
4. Liga os outputs de um nó aos inputs do seguinte
5. Clica **Save** → **Run Workflow** para testar

> 📖 **Referência:** [Build a workflow in Microsoft Foundry](https://learn.microsoft.com/azure/foundry/agents/concepts/workflow)

---

## Resultado Esperado

- Pipeline funcional com múltiplas chamadas encadeadas ao modelo
- Compreensão de como orquestrar prompt chaining via código e via portal
