# Lab 04 — Multi-Agent Workflows

Step-by-step guide to creating **multi-agent workflows** with the Foundry Agent Service.

> 📖 **Official reference:** [Build a workflow in Microsoft Foundry](https://learn.microsoft.com/azure/foundry/agents/concepts/workflow)

---

## Step 1 — Understand Multi-Agent Workflows

In Foundry, you can create **multi-agent workflows** in two ways:

1. **Workflow Agents (portal)** — visual orchestration with Sequential, Group Chat, or Human-in-the-Loop patterns
2. **Connected Agents (code)** — via `ConnectedAgentTool` in the Python SDK, where a main agent delegates to sub-agents

---

## Step 2 — Create Specialized Agents in the Portal

1. In the Foundry portal → **Build** → **Agents**
2. Create **2-3 prompt agents** with specific instructions each:
   - E.g., `research-agent` — specialized in research
   - E.g., `analysis-agent` — specialized in data analysis
   - E.g., `writing-agent` — specialized in writing responses
3. For each agent, define the **Instructions** and the **Model** (`gpt-4o`)

---

## Step 3 — Create a Multi-Agent Workflow in the Portal

1. In the Foundry portal → **Build** → **Create new workflow**
2. Choose the **Sequential** pattern (or **Group chat** for dynamic collaboration)
3. Add the agents created in Step 2 as workflow nodes:
   - Click **+** → **Invoke agent** → select an existing agent
   - Repeat for each agent
4. Configure the execution order and inputs/outputs
5. Click **Save**

---

## Step 4 — Test the Workflow

1. In the workflow editor, click **Run Workflow**
2. Send a message that requires collaboration between agents
3. Observe each node executing in the visualizer
4. Check the responses in the chat window

---

## Step 5 — Implement via Code

1. Open the notebook [`lab04b-agent-workflows.ipynb`](lab04b-agent-workflows.ipynb)
2. Run the cells — the notebook demonstrates:
   - Creating agents via `AIProjectClient`
   - Connecting agents with `ConnectedAgentTool`
   - Orchestrating the multi-agent workflow programmatically

---

## Expected Result

- Functional multi-agent workflow with specialized agents
- Agents visible and connected in the Foundry portal
