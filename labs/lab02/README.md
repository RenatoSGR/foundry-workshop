# Lab 02 — Agents in Microsoft Foundry

Step-by-step guide to creating agents with **tools** and with the **Agent Service** in Foundry.

> 📖 **Official reference:** [What is Microsoft Foundry Agent Service?](https://learn.microsoft.com/azure/foundry/agents/overview)

---

## Part A — Agents with the Responses API (lab02)

### Step 1 — Understand the Agent Concept

An **Agent** in Foundry is an assistant that can:
- Use **tools** (code interpreter, file search, web search, functions)
- Maintain context throughout a conversation
- Execute actions autonomously based on instructions

Foundry supports three types of agents:
- **Prompt agents** — configured via the portal, no code required
- **Workflow agents** (preview) — visual multi-agent orchestration
- **Hosted agents** (preview) — containers with custom code

### Step 2 — Create an Agent via Code

1. Open the notebook [`lab02-agentes.ipynb`](lab02-agentes.ipynb)
2. Run the cells in order — the notebook demonstrates:
   - Creating an agent with the Azure OpenAI **Responses API**
   - Defining **tools** (functions) the agent can call
   - Processing **function calling** — the model decides when to use each tool

### Step 3 — Test in the Portal (Model Playground)

1. In the Foundry portal → **Build** → **Models** → select the `gpt-4o` deployment
2. In the Playground, expand the **Tools** section and add **Code interpreter** or a custom function
3. Send a message that requires using the tool and observe the flow

---

## Part B — Agents with the Agent Service (lab02.1)

### Step 1 — Create a Prompt Agent in the Portal

1. In the Foundry portal → **Build** → **Agents**
2. Click **+ New agent** → choose **Prompt agent**
3. Configure:
   - **Name**: e.g., `workshop-assistant`
   - **Instructions**: define the agent's behavior
   - **Model**: select `gpt-4o`
4. The agent is created automatically

> ⚠️ **Note:** After naming the agent, you cannot change it. In code, you reference the agent as `<agent_name>:<version>`.

### Step 2 — Add Tools to the Agent

1. In the agent configuration, **Tools** section
2. Add available tools (Code Interpreter, File Search, Web Search)
3. For more tools, go to **Build** → **Tools** to explore the tool catalog (including MCP servers)
4. Save the changes

### Step 3 — Test in the Agents Playground

1. The **Agents Playground** opens integrated in the agent panel
2. Send messages and observe the agent using the tools
3. In the **Code** tab, you can copy the code or open directly in **VS Code for the Web**

### Step 4 — Consume via Code

1. Open the notebook [`lab02.1-agentes.ipynb`](lab02.1-agentes.ipynb)
2. Run the cells — the notebook demonstrates:
   - Creating an agent with `AIProjectClient`
   - The **Agent → Conversation → Response** cycle
   - The agent becomes visible in the Foundry portal

---

## Expected Result

- Agent created and functional with tools (function calling)
- Agent visible and testable in the Foundry portal
