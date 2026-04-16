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
│  (managed infrastructure) │  (created/connected via Foundry IQ)
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
| **Azure AI Search** | Provides the underlying indexing and search infrastructure. |

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
3. Select the files you want to index (PDF, Markdown, TXT, Word, etc.)
4. Click **Upload**

> 💡 **Tip:** Organize documents into folders within the container for easier management. AI Search can navigate the folder structure automatically.

---

## Step 2 — Create Azure AI Search

AI Search provides the indexing and search infrastructure used by Foundry IQ.

### In the Azure Portal:

1. Search for **AI Search** and click **+ Create**
2. Fill in the fields:
   - **Resource group:** the same as the Foundry project
   - **Service name:** a unique name (e.g., `search-workshop-knowledge`)
   - **Region:** the same region as the Foundry project
   - **Pricing tier:** **Basic** (sufficient for the workshop; the Free tier does not support agentic retrieval)
3. Click **Review + Create** → **Create**

> ⚠️ **Important:** AI Search and the Storage Account should be in the **same region** for best performance. For proof-of-concept, you can use the **free tier** of AI Search with a free token allocation for agentic retrieval.

> 💡 **Note:** In the new Foundry, you can create or connect the AI Search service directly from the Foundry portal (Step 4), without needing to create it manually first. The manual step is useful if you want more control over the configuration.

---

## Step 3 — Deploy an Embedding Model in Foundry

The embedding model is required to convert text into numerical vectors, enabling semantic search. Foundry IQ automates embedding generation during indexing, but it needs a deployed model.

### Why an embedding model?

- Converts text into high-dimensional vectors that capture **semantic meaning**
- Allows finding relevant documents even if they don't contain the exact words from the query
- Foundry IQ uses it automatically for chunking and vector embedding generation

### In the Microsoft Foundry Portal ([ai.azure.com](https://ai.azure.com)):

1. Open your **project**
2. Go to **Models + endpoints** (side menu)
3. Click **+ Deploy model** → **Deploy base model**
4. Search for and select **text-embedding-ada-002** (or **text-embedding-3-small** for better performance)
5. Set the **deployment name** (e.g., `text-embedding-ada-002`)
6. Select the capacity (tokens per minute) — the minimum is sufficient for the workshop
7. Click **Deploy**

> 💡 **Note:** `text-embedding-3-small` is newer and more efficient. Both work. Foundry IQ needs an Azure OpenAI embedding model for agentic retrieval.

---

## Step 4 — Create Knowledge Base and Knowledge Sources in Foundry IQ

In the new Foundry, knowledge base creation uses **Foundry IQ**, which automates chunking, embedding, and indexing — and supports **agentic retrieval** (query decomposition, parallel search, reranking, and citations).

### In the Microsoft Foundry Portal ([ai.azure.com](https://ai.azure.com)):

1. Make sure the **New Foundry** toggle is **ON** (top corner)
2. Open your **project**
3. In the top menu, click **Build**

### Create/connect the AI Search service:

4. In the **Knowledge** tab:
   - Click to **create or connect** to an existing AI Search service (from Step 2)
   - If you haven't created one yet, Foundry can create one for you

### Create a Knowledge Source:

5. Click **Add knowledge source**
6. Select **Azure Blob Storage** as the source type
7. Configure the connection:
   - Select the **Storage Account** from Step 1
   - Select the `documentos` container
8. Foundry IQ automatically:
   - Reads the documents from Storage
   - Splits them into chunks (automatic document chunking)
   - Generates vector embeddings using the model from Step 3
   - Extracts metadata
   - Indexes everything in AI Search

### Create the Knowledge Base:

9. Still in the **Knowledge** tab, click **Create knowledge base**
10. Add the knowledge source(s) created above
11. Configure the retrieval parameters:
    - **Retrieval reasoning effort:** `low` for the workshop (options: minimal, low, medium)
    - This controls the level of LLM processing for query planning
12. Click **Create**

### Wait for indexing:

- Progress is visible on the Knowledge Base page
- When the status changes to **Ready**, it's ready to use
- You can configure **recurring indexer runs** for incremental data refresh

> 💡 **Note:** A knowledge base can contain **multiple knowledge sources** (e.g., Blob Storage + SharePoint + web). Multiple agents can **share the same knowledge base**.

---

## Step 5 — Connect the Knowledge Base to an Agent

### In the Foundry Portal (Agents tab):

1. In the **Build** menu, go to the **Agents** tab
2. Create a new agent or select an existing one
3. In **Knowledge**, connect the knowledge base created in Step 4
4. Use the **Playground** to send messages and test the agent

The agent now uses **agentic retrieval** from Foundry IQ:
- Breaks down complex questions into sub-queries
- Executes searches in parallel across knowledge sources
- Performs semantic reranking of results
- Returns answers with **citations** to source documents
- Respects **permissions** (ACLs) and Microsoft Purview sensitivity labels

### In the Foundry Playground:

1. Ask questions about the content of your documents
2. Verify that responses include **citations** with links to the original documents
3. Test with complex questions that require cross-referencing information from multiple documents

> 📖 For code integration, see: [Connect Foundry IQ to Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/how-to/foundry-iq/)

---

## Summary of Created Resources

| Resource | Purpose |
|----------|---------|
| **Storage Account** + Container | Store original documents |
| **Azure AI Search** | Indexing and search infrastructure (managed by Foundry IQ) |
| **Embedding Model** (deployment) | Convert text into semantic vectors (used automatically by Foundry IQ) |
| **Knowledge Source** (Foundry IQ) | Connection to data store with automatic chunking and embeddings |
| **Knowledge Base** (Foundry IQ) | Orchestrate agentic retrieval with citations and permissions |

---

## Required Environment Variables

If you want to use the Knowledge Base via code, add to your `.env` file:

```env
AZURE_SEARCH_ENDPOINT=https://<search-name>.search.windows.net
AZURE_SEARCH_KEY=<search-admin-key>
EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

---

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Indexing fails | Check that AI Search has permissions to access Storage (same region, or configure managed identity) |
| Poor search results | Increase the **retrieval reasoning effort** (from minimal to medium) in the knowledge base |
| Knowledge Source not indexing | Verify the embedding model is deployed and accessible in the project |
| Agent doesn't find documents | Confirm the knowledge base is **Ready** and connected to the agent |
| "New Foundry" toggle not visible | Make sure you're at [ai.azure.com](https://ai.azure.com) with the new portal enabled |
| Permission errors | Configure managed identities instead of keys for production environments |

---

## References

- [What is Foundry IQ?](https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq)
- [Tutorial: Build an end-to-end agentic retrieval solution](https://learn.microsoft.com/azure/search/search-how-to-agentic-retrieval-solution)
- [Microsoft Foundry Portal](https://ai.azure.com)
