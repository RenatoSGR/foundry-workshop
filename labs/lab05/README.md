# Lab 05 — Knowledge Base com Foundry IQ

Guia passo a passo para criar uma **Knowledge Base** usando **Foundry IQ** no Microsoft Foundry. O Foundry IQ é a camada de conhecimento gerida que liga dados estruturados e não estruturados (Azure Storage, SharePoint, OneLake, web) para que agentes possam aceder a respostas com permissões e citações.

> 📖 **Referência oficial:** [What is Foundry IQ?](https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq)

---

## Arquitetura (Foundry IQ)

```
Documentos (PDF, MD, Word, etc.)
        │
        ▼
┌──────────────────────────┐
│  Azure Storage            │  Armazenamento de documentos
│  (Blob Container)         │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Knowledge Source          │  Conexão ao data store
│  (Foundry IQ)             │  (chunking + embeddings automáticos)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Azure AI Search          │  Indexação + pesquisa vetorial
│  (infraestrutura gerida)  │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Knowledge Base           │  Agentic Retrieval
│  (Foundry IQ)             │  (multi-query, reranking, citações)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Agente                   │  Usa a Knowledge Base para RAG
│  (Foundry Agent Service)  │
└──────────────────────────┘
```

### Conceitos-chave do Foundry IQ

| Componente | Descrição |
|------------|-----------|
| **Knowledge Base** | Recurso de topo que orquestra o agentic retrieval. Define quais knowledge sources consultar e parâmetros de comportamento (retrieval reasoning effort: minimal, low, medium). |
| **Knowledge Source** | Conexão a conteúdo indexado ou remoto (Azure Blob Storage, SharePoint, OneLake, web). Uma knowledge base pode ter múltiplas knowledge sources. |
| **Agentic Retrieval** | Pipeline multi-query que decompõe perguntas complexas em sub-queries, executa-as em paralelo, faz reranking semântico e devolve respostas unificadas com citações. |
| **Azure AI Search** | Fornece a infraestrutura subjacente de indexação e pesquisa. É **obrigatório** para o Foundry IQ. |

---

## Passo 1 — Criar uma Storage Account e Container

A Storage Account serve como repositório central dos documentos que vão alimentar a Knowledge Base.

### No Portal Azure ([portal.azure.com](https://portal.azure.com)):

1. Procura por **Storage accounts** e clica em **+ Create**
2. Preenche os campos:
   - **Resource group:** seleciona o mesmo resource group do teu projeto Foundry
   - **Storage account name:** um nome único (ex: `stworkshopknowledge`)
   - **Region:** a mesma região do teu projeto Foundry
   - **Performance:** Standard
   - **Redundancy:** LRS (suficiente para workshop)
3. Clica **Review + Create** → **Create**

### Criar o Container de documentos:

1. Abre a Storage Account criada
2. No menu lateral, vai a **Data storage → Containers**
3. Clica **+ Container**
4. Define o nome: `documentos`
5. Nível de acesso: **Private**
6. Clica **Create**

### Upload dos documentos:

1. Abre o container `documentos`
2. Clica **Upload**
3. Seleciona os ficheiros da pasta `data/documentos/` deste repositório
4. Clica **Upload**

---

## Passo 2 — Criar o Azure AI Search

O AI Search fornece a infraestrutura de indexação e pesquisa usada pelo Foundry IQ.

### No Portal Azure:

1. Procura por **AI Search** e clica em **+ Create**
2. Preenche os campos:
   - **Resource group:** o mesmo do projeto Foundry
   - **Service name:** um nome único (ex: `search-workshop-knowledge`)
   - **Region:** a mesma região do projeto Foundry
   - **Pricing tier:** **Basic** (suficiente para o workshop)
3. Clica **Review + Create** → **Create**
4. Aguarda o deployment concluir

---

## Passo 3 — Configurar a Knowledge Base via Foundry IQ

### No portal Microsoft Foundry ([ai.azure.com](https://ai.azure.com)):

1. Certifica-te que o toggle **New Foundry** está ativo no banner superior
2. Seleciona o teu **projeto**
3. No menu superior, clica em **Build**
4. No painel esquerdo, seleciona o separador **Knowledge**
5. Cria ou liga ao teu Azure AI Search (criado no Passo 2)
6. Clica em **+ Add knowledge source**:
   - Seleciona **Azure Blob Storage** como tipo de source
   - Liga à Storage Account e container `documentos` criados no Passo 1
   - O Foundry IQ faz automaticamente: chunking, geração de embeddings e indexação
7. Configura o **Retrieval reasoning effort** (ex: `medium` para melhor qualidade)
8. Aguarda a indexação concluir

---

## Passo 4 — Ligar a Knowledge Base a um Agente

1. No portal Foundry → **Build** → **Agents**
2. Seleciona um agente existente ou cria um novo
3. Na configuração do agente, adiciona a **Knowledge Base** como fonte de conhecimento
4. Guarda as alterações

---

## Passo 5 — Testar no Agents Playground

1. No Agents Playground do agente configurado
2. Envia perguntas sobre o conteúdo dos documentos carregados
3. Verifica que as respostas incluem **citações** dos documentos originais
4. Testa com perguntas complexas para observar o **agentic retrieval** em ação

---

## Resultado Esperado

- Knowledge Base configurada e funcional com Foundry IQ
- Agente com acesso a documentos via agentic retrieval
- Respostas com citações dos documentos carregados
