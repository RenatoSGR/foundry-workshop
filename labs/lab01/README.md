# Lab 01 — Models and Deployment

Step-by-step guide to deploying and consuming models in **Microsoft Foundry**.

> 📖 **Official reference:** [Deploy models in the Foundry portal](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/deploy-foundry-models)

---

## Step 1 — Access the Model Catalog

1. Open the **Microsoft Foundry** portal → [ai.azure.com](https://ai.azure.com)
2. Make sure the **New Foundry** toggle is active in the top banner
3. Select your **project**
4. In the top menu, click **Discover** → in the left panel select **Models**
5. Explore the catalog — thousands of models are available (OpenAI, Meta, Mistral, DeepSeek, etc.)

---

## Step 2 — Deploy a Chat Model (GPT-4o)

1. In the model catalog, search for **GPT-4o** and select it
2. Click **Deploy** → **Custom settings** (or **Default settings** for quick setup)
3. Set the **Deployment name**: `gpt-4o`
4. Choose the tokens-per-minute capacity (the minimum is sufficient for the workshop)
5. Click **Deploy**
6. Wait until the status changes to **Succeeded**

---

## Step 3 — Deploy an Embeddings Model

1. Go back to the catalog: **Discover** → **Models**
2. Search for **text-embedding-ada-002** (or `text-embedding-3-small`)
3. Click **Deploy** → **Custom settings**
4. Set the **Deployment name**: `text-embedding-ada-002`
5. Click **Deploy**

---

## Step 4 — Verify the Deployments

1. In the top menu, click **Build** → in the left panel select **Models**
2. Verify that both deployments appear with status **Succeeded**

---

## Step 5 — Test in the Playground

1. In the deployments list (**Build** → **Models**), click on the `gpt-4o` deployment
2. The **Playground** opens automatically
3. Send a test message (e.g., "Hello, how are you?")
4. Verify that the model responds correctly
5. Try adjusting parameters in the side panel (temperature, max tokens, etc.)

---

## Step 6 — Consume via Code (Notebook)

1. Open the notebook [`lab01-modelos.ipynb`](lab01-modelos.ipynb)
2. Make sure `.env` is configured (`python setup_env.py`)
3. Run the cells in order — the notebook demonstrates:
   - Connecting to the Foundry endpoint
   - Making **chat completions** calls
   - Adjusting parameters (`temperature`, `max_tokens`, etc.)

---

## Expected Result

- Two models deployed and operational in Foundry
- Model responses via Playground and via Python code
