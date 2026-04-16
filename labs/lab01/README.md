# Lab 01 — Modelos e Deployment

Guia passo a passo para deployar e consumir modelos no **Microsoft Foundry**.

> 📖 **Referência oficial:** [Deploy models in the Foundry portal](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/deploy-foundry-models)

---

## Passo 1 — Aceder ao Catálogo de Modelos

1. Abre o portal **Microsoft Foundry** → [ai.azure.com](https://ai.azure.com)
2. Certifica-te que o toggle **New Foundry** está ativo no banner superior
3. Seleciona o teu **projeto**
4. No menu superior, clica em **Discover** → no painel esquerdo seleciona **Models**
5. Explora o catálogo — estão disponíveis milhares de modelos (OpenAI, Meta, Mistral, DeepSeek, etc.)

---

## Passo 2 — Deployar um Modelo de Chat (GPT-4o)

1. No catálogo de modelos, procura por **GPT-4o** e seleciona-o
2. Clica em **Deploy** → **Custom settings** (ou **Default settings** para configuração rápida)
3. Define o **Deployment name**: `gpt-4o`
4. Escolhe a capacidade de tokens por minuto (o mínimo é suficiente para o workshop)
5. Clica **Deploy**
6. Aguarda até o estado mudar para **Succeeded**

---

## Passo 3 — Deployar um Modelo de Embeddings

1. Volta ao catálogo: **Discover** → **Models**
2. Procura por **text-embedding-ada-002** (ou `text-embedding-3-small`)
3. Clica em **Deploy** → **Custom settings**
4. Define o **Deployment name**: `text-embedding-ada-002`
5. Clica **Deploy**

---

## Passo 4 — Verificar os Deployments

1. No menu superior, clica em **Build** → no painel esquerdo seleciona **Models**
2. Verifica que ambos os deployments aparecem com estado **Succeeded**

---

## Passo 5 — Testar no Playground

1. Na lista de deployments (**Build** → **Models**), clica no deployment `gpt-4o`
2. O **Playground** abre automaticamente
3. Envia uma mensagem de teste (ex: "Olá, como estás?")
4. Verifica que o modelo responde corretamente
5. Experimenta ajustar parâmetros no painel lateral (temperature, max tokens, etc.)

---

## Passo 6 — Consumir via Código (Notebook)

1. Abre o notebook [`lab01-modelos.ipynb`](lab01-modelos.ipynb)
2. Certifica-te que o `.env` está configurado (`python setup_env.py`)
3. Executa as células por ordem — o notebook demonstra:
   - Ligar ao endpoint do Foundry
   - Fazer chamadas de **chat completions**
   - Ajustar parâmetros (`temperature`, `max_tokens`, etc.)

---

## Resultado Esperado

- Dois modelos deployados e operacionais no Foundry
- Respostas do modelo via Playground e via código Python
