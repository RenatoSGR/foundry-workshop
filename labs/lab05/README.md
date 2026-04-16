# Lab 05 — Knowledge Base with Foundry IQ

Step-by-step guide to creating a **Knowledge Base** using **Foundry IQ** in Microsoft Foundry. Foundry IQ is the managed knowledge layer that connects structured and unstructured data (Azure Storage, SharePoint, OneLake, web) so that agents can access answers with permissions and citations.

> 📖 **Official reference:** [What is Foundry IQ?](https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq)

---

## Architecture (Foundry IQ)

```
Documents (PDF, MD, Word, etc.)
        │
        ▼
┌──────────────────────────┐
│  Azure Storage            │  Document storage
│  (Blob Container)         │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Knowledge Source          │  Connection to data store
│  (Foundry IQ)             │  (automatic chunking + embeddings)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Azure AI Search          │  Indexing + vector search
│  (managed infrastructure) │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Knowledge Base           │  Agentic Retrieval
│  (Foundry IQ)             │  (multi-query, reranking, citations)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Agent                    │  Uses Knowledge Base for RAG
│  (Foundry Agent Service)  │
└──────────────────────────┘
```

### Key Foundry IQ Concepts

| Component | Description |
|-----------|-------------|
| **Knowledge Base** | Top-level resource that orchestrates agentic retrieval. Defines which knowledge sources to query and behavior parameters (retrieval reasoning effort: minimal, low, medium). |
| **Knowledge Source** | Connection to indexed or remote content (Azure Blob Storage, SharePoint, OneLake, web). A knowledge base can have multiple knowledge sources. |
| **Agentic Retrieval** | Multi-query pipeline that breaks down complex questions into sub-queries, executes them in parallel, performs semantic reranking, and returns unified answers with citations. |
| **Azure AI Search** | Provides the underlying indexing and search infrastructure. It is **required** for Foundry IQ. |

---

## Step 1 — Create a Storage Account and Container

The Storage Account serves as the central repository for the documents that will feed the Knowledge Base.

### In the Azure Portal ([portal.azure.com](https://portal.azure.com)):

1. Search for **Storage accounts** and click **+ Create**
2. Fill in the fields:
   - **Resource group:** select the same resource group as your Foundry project
   - **Storage account name:** a unique name (e.g., `stworkshopknowledge`)
   - **Region:** the same region as your Foundry project
   - **Performance:** Standard
   - **Redundancy:** LRS (sufficient for the workshop)
3. Click **Review + Create** → **Create**

### Create the documents container:

1. Open the created Storage Account
2. In the side menu, go to **Data storage → Containers**
3. Click **+ Container**
4. Set the name: `documentos`
5. Access level: **Private**
6. Click **Create**

### Upload the documents:

1. Open the `documentos` container
2. Click **Upload**
3. Select the files from the `data/documentos/` folder in this repository
4. Click **Upload**

---

## Step 2 — Create Azure AI Search

AI Search provides the indexing and search infrastructure used by Foundry IQ.

### In the Azure Portal:

1. Search for **AI Search** and click **+ Create**
2. Fill in the fields:
   - **Resource group:** the same as the Foundry project
   - **Service name:** a unique name (e.g., `search-workshop-knowledge`)
   - **Region:** the same region as the Foundry project
   - **Pricing tier:** **Basic** (sufficient for the workshop)
3. Click **Review + Create** → **Create**
4. Wait for the deployment to complete

---

## Step 3 — Configure the Knowledge Base via Foundry IQ

### In the Microsoft Foundry portal ([ai.azure.com](https://ai.azure.com)):

1. Make sure the **New Foundry** toggle is active in the top banner
2. Select your **project**
3. In the top menu, click **Build**
4. In the left panel, select the **Knowledge** tab
5. Create or connect to your Azure AI Search (created in Step 2)
6. Click **+ Add knowledge source**:
   - Select **Azure Blob Storage** as the source type
   - Connect to the Storage Account and `documentos` container created in Step 1
   - Foundry IQ automatically handles: chunking, embedding generation, and indexing
7. Configure the **Retrieval reasoning effort** (e.g., `medium` for better quality)
8. Wait for indexing to complete

---

## Step 4 — Connect the Knowledge Base to an Agent

1. In the Foundry portal → **Build** → **Agents**
2. Select an existing agent or create a new one
3. In the agent configuration, add the **Knowledge Base** as a knowledge source
4. Save the changes

---

## Step 5 — Test in the Agents Playground

1. In the Agents Playground of the configured agent
2. Ask questions about the content of the uploaded documents
3. Verify that responses include **citations** from the original documents
4. Test with complex questions to observe **agentic retrieval** in action

---

## Expected Result

- Knowledge Base configured and functional with Foundry IQ
- Agent with access to documents via agentic retrieval
- Responses with citations from the uploaded documents
