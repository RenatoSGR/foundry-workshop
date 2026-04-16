# Lab 03 — Workflows with LLM

Step-by-step guide to creating **chained call pipelines** to the model (prompt chaining) in Foundry.

> 📖 **Official reference:** [Microsoft Foundry Playgrounds](https://learn.microsoft.com/azure/foundry/concepts/concept-playgrounds)

---

## Step 1 — Understand LLM Workflows

An **LLM Workflow** is a pipeline where each step uses the model for a specific task:
- **Step 1**: Analyze the input (e.g., extract entities)
- **Step 2**: Process (e.g., classify, translate)
- **Step 3**: Generate final output (e.g., structured summary)

Each step receives the output of the previous one as context.

---

## Step 2 — Test Prompt Chaining in the Playground

1. In the Foundry portal → **Build** → **Models** → select the `gpt-4o` deployment
2. In the Playground, test each step individually:
   - Send a text and ask the model to **extract entities**
   - Copy the result and ask it to **classify**
   - Copy and ask it to **generate a summary**
3. Observe how each step transforms the information

> 💡 **Tip:** You can use **Compare mode** (button in the top-right corner of the Playground) to test the same prompt on up to 3 models simultaneously.

---

## Step 3 — Automate via Code

1. Open the notebook [`lab03-model-workflows.ipynb`](lab03-model-workflows.ipynb)
2. Run the cells in order — the notebook demonstrates:
   - Chaining multiple calls to the model
   - Passing the output of one call as input to the next
   - Building text processing pipelines

---

## Step 4 — Explore Workflows in the Portal

In Foundry, you can create **Workflow Agents** that orchestrate actions visually:

1. In the Foundry portal → **Build** → click **Create new workflow**
2. Choose a template (e.g., **Sequential**) or create from scratch
3. Add chained **Invoke agent** nodes
4. Connect the outputs of one node to the inputs of the next
5. Click **Save** → **Run Workflow** to test

> 📖 **Reference:** [Build a workflow in Microsoft Foundry](https://learn.microsoft.com/azure/foundry/agents/concepts/workflow)

---

## Expected Result

- Functional pipeline with multiple chained calls to the model
- Understanding of how to orchestrate prompt chaining via code and via the portal
