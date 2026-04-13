# 📚 Lab 04 - Knowledge Base com Foundry IQ

Guia passo a passo para criar uma **Knowledge Base** usando **Foundry IQ** no novo portal Microsoft Foundry. O Foundry IQ é a camada de conhecimento gerida que liga dados estruturados e não estruturados (Azure Storage, SharePoint, OneLake, web) para que agentes possam aceder a respostas com permissões e citações.

> 📖 **Referência oficial:** [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq?tabs=portal)

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
│  (infraestrutura gerida)  │  (criado/conectado via Foundry IQ)
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
| **Azure AI Search** | Fornece a infraestrutura subjacente de indexação e pesquisa. |

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
3. Seleciona os ficheiros que queres indexar (PDF, Markdown, TXT, Word, etc.)
4. Clica **Upload**

> 💡 **Dica:** Organiza os documentos em pastas dentro do container para facilitar a gestão. O AI Search consegue navegar a estrutura de pastas automaticamente.

---

## Passo 2 — Criar o Azure AI Search

O AI Search fornece a infraestrutura de indexação e pesquisa usada pelo Foundry IQ.

### No Portal Azure:

1. Procura por **AI Search** e clica em **+ Create**
2. Preenche os campos:
   - **Resource group:** o mesmo do projeto Foundry
   - **Service name:** um nome único (ex: `search-workshop-knowledge`)
   - **Region:** a mesma região do projeto Foundry
   - **Pricing tier:** **Basic** (suficiente para workshop; o tier Free não suporta agentic retrieval)
3. Clica **Review + Create** → **Create**

> ⚠️ **Importante:** O AI Search e a Storage Account devem estar na **mesma região** para melhor performance. Para proof-of-concept, podes usar o **free tier** do AI Search com uma alocação gratuita de tokens para agentic retrieval.

> 💡 **Nota:** No novo Foundry, podes criar ou conectar o serviço AI Search diretamente a partir do portal Foundry (Passo 4), sem necessidade de o criar manualmente primeiro. O passo manual é útil se quiseres mais controlo sobre a configuração.

---

## Passo 3 — Deployar um Embedding Model no Foundry

O modelo de embeddings é necessário para converter texto em vetores numéricos, permitindo pesquisa semântica. O Foundry IQ automatiza a geração de embeddings durante a indexação, mas precisa de um modelo deployado.

### Porquê um modelo de embeddings?

- Converte texto em vetores de alta dimensão que capturam o **significado semântico**
- Permite encontrar documentos relevantes mesmo que não contenham as palavras exatas da pergunta
- O Foundry IQ usa-o automaticamente para chunking e geração de vector embeddings

### No Portal Microsoft Foundry ([foundry.microsoft.com](https://foundry.microsoft.com)):

1. Abre o teu **projeto**
2. Vai a **Models + endpoints** (menu lateral)
3. Clica **+ Deploy model** → **Deploy base model**
4. Procura e seleciona **text-embedding-ada-002** (ou **text-embedding-3-small** para melhor performance)
5. Define o **deployment name** (ex: `text-embedding-ada-002`)
6. Seleciona a capacidade (tokens por minuto) — o mínimo é suficiente para workshop
7. Clica **Deploy**

> 💡 **Nota:** O `text-embedding-3-small` é mais recente e eficiente. Ambos funcionam. O Foundry IQ precisa de um modelo de embeddings do Azure OpenAI para o agentic retrieval.

---

## Passo 4 — Criar Knowledge Base e Knowledge Sources no Foundry IQ

No novo Foundry, a criação de knowledge bases usa o **Foundry IQ**, que automatiza chunking, embedding e indexação — e suporta **agentic retrieval** (decomposição de queries, pesquisa paralela, reranking e citações).

### No Portal Microsoft Foundry ([foundry.microsoft.com](https://foundry.microsoft.com)):

1. Certifica-te que o toggle **New Foundry** está **ON** (canto superior)
2. Abre o teu **projeto**
3. No menu superior, clica em **Build**

### Criar/conectar o serviço AI Search:

4. No tab **Knowledge**:
   - Clica para **criar ou conectar** a um serviço AI Search existente (o do Passo 2)
   - Se ainda não criaste, o Foundry pode criar um por ti

### Criar uma Knowledge Source:

5. Clica **Add knowledge source**
6. Seleciona **Azure Blob Storage** como tipo de source
7. Configura a conexão:
   - Seleciona a **Storage Account** do Passo 1
   - Seleciona o container `documentos`
8. O Foundry IQ automaticamente:
   - Lê os documentos do Storage
   - Divide em chunks (document chunking automático)
   - Gera vector embeddings usando o modelo do Passo 3
   - Extrai metadata
   - Indexa tudo no AI Search

### Criar a Knowledge Base:

9. Ainda no tab **Knowledge**, clica **Create knowledge base**
10. Adiciona a(s) knowledge source(s) criada(s)
11. Configura os parâmetros de retrieval:
    - **Retrieval reasoning effort:** `low` para workshop (opções: minimal, low, medium)
    - Isto controla o nível de processamento LLM para planeamento de queries
12. Clica **Create**

### Aguarda a indexação:

- O progresso é visível na página da Knowledge Base
- Quando o estado mudar para **Ready**, está pronta para usar
- Podes configurar **indexer runs recorrentes** para refresh incremental dos dados

> 💡 **Nota:** Uma knowledge base pode conter **múltiplas knowledge sources** (ex: Blob Storage + SharePoint + web). Múltiplos agentes podem **partilhar a mesma knowledge base**.

---

## Passo 5 — Conectar a Knowledge Base a um Agente

### No Portal Foundry (tab Agents):

1. No menu **Build**, vai ao tab **Agents**
2. Cria um novo agente ou seleciona um existente
3. Em **Knowledge**, conecta a knowledge base criada no Passo 4
4. Usa o **Playground** para enviar mensagens e testar o agente

O agente agora usa **agentic retrieval** do Foundry IQ:
- Decompõe perguntas complexas em sub-queries
- Executa pesquisas em paralelo nas knowledge sources
- Faz reranking semântico dos resultados
- Devolve respostas com **citações** para os documentos fonte
- Respeita **permissões** (ACLs) e etiquetas de sensibilidade do Microsoft Purview

### No Playground do Foundry:

1. Faz perguntas sobre o conteúdo dos teus documentos
2. Verifica que as respostas incluem **citações** com links para os documentos originais
3. Testa com perguntas complexas que exigem cruzar informação de múltiplos documentos

### Por código (Lab 04):

Consulta o notebook [lab04-knowledge-rag.ipynb](lab04-knowledge-rag.ipynb) para exemplos de:
- Criação de embeddings programaticamente
- Pesquisa vetorial com AI Search
- Pipeline RAG completo (pesquisa + geração)

> 📖 Para integração por código, consulta: [Connect Foundry IQ to Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/foundry-iq/)

---

## Resumo dos Recursos Criados

| Recurso | Propósito |
|---------|-----------|
| **Storage Account** + Container | Armazenar documentos originais |
| **Azure AI Search** | Infraestrutura de indexação e pesquisa (gerida pelo Foundry IQ) |
| **Embedding Model** (deployment) | Converter texto em vetores semânticos (usado automaticamente pelo Foundry IQ) |
| **Knowledge Source** (Foundry IQ) | Conexão ao data store com chunking e embeddings automáticos |
| **Knowledge Base** (Foundry IQ) | Orquestrar agentic retrieval com citações e permissões |

---

## Variáveis de Ambiente Necessárias

Se quiseres usar a Knowledge Base por código, adiciona ao ficheiro `.env`:

```env
AZURE_SEARCH_ENDPOINT=https://<nome-do-search>.search.windows.net
AZURE_SEARCH_KEY=<admin-key-do-search>
EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| Indexação falha | Verifica se o AI Search tem permissões para aceder ao Storage (mesma região, ou configura managed identity) |
| Resultados de pesquisa fracos | Aumenta o **retrieval reasoning effort** (de minimal para medium) na knowledge base |
| Knowledge Source não indexa | Verifica que o embedding model está deployado e acessível no projeto |
| Agente não encontra documentos | Confirma que a knowledge base está **Ready** e conectada ao agente |
| Toggle "New Foundry" não aparece | Garante que estás em [foundry.microsoft.com](https://foundry.microsoft.com) e não no portal antigo ai.azure.com |
| Erro de permissões | Configura managed identities em vez de keys para ambientes de produção |

---

## Referências

- [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq?tabs=portal)
- [Tutorial: Build an end-to-end agentic retrieval solution](https://learn.microsoft.com/en-us/azure/search/search-how-to-agentic-retrieval-solution)
- [Microsoft Foundry Portal](https://foundry.microsoft.com)
