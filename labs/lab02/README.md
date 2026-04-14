# Lab 02 — Modelos e Deployment

Guia passo a passo para deployar e consumir modelos no **Microsoft Foundry v2**.

---

## Passo 1 — Aceder ao Catálogo de Modelos

1. Abre o portal **Microsoft Foundry** → [ai.azure.com](https://ai.azure.com)
2. Seleciona o teu **projeto**
3. No menu lateral, clica em **Models + endpoints**
4. Explora o catálogo — estão disponíveis 11000+ modelos (OpenAI, Meta, Mistral, etc.)

---

## Passo 2 — Deployar um Modelo de Chat (GPT-4o)

1. Em **Models**, clica em **+ Deploy model** → **Deploy base model**
2. Procura por **GPT-4o** e seleciona-o
3. Define o **Deployment name**: `gpt-4o`
4. Escolhe a capacidade de tokens por minuto (o mínimo é suficiente para o workshop)
5. Clica **Deploy**
6. Aguarda até o estado mudar para **Succeeded**

---

## Passo 3 — Deployar um Modelo de Embeddings

1. Repete o processo: **+ Deploy model** → **Deploy base model**
2. Procura por **text-embedding-ada-002** (ou `text-embedding-3-small`)
3. Define o **Deployment name**: `text-embedding-ada-002`
4. Clica **Deploy**

---

## Passo 4 — Testar no Playground

1. Em **Models**, clica no deployment `gpt-4o`
2. Abre o **Playground** (botão no topo)
3. Envia uma mensagem de teste (ex: "Olá, como estás?")
4. Verifica que o modelo responde corretamente

---

## Passo 5 — Consumir via Código (Notebook)

1. Abre o notebook [`lab02-modelos.ipynb`](lab02-modelos.ipynb)
2. Certifica-te que o `.env` está configurado (`python setup_env.py`)
3. Executa as células por ordem — o notebook demonstra:
   - Ligar ao endpoint com `azure-ai-inference`
   - Fazer chamadas de **chat completions**
   - Ajustar parâmetros (`temperature`, `max_tokens`, etc.)

---

## Resultado Esperado

- Dois modelos deployados e operacionais no Foundry
- Respostas do modelo via Playground e via código Python
