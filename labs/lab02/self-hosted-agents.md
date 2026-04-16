# Lab 02.3 — Hosted Agents in Microsoft Foundry

Step-by-step guide to building and deploying **Hosted Agents** — containerized agents with custom code that run on Foundry-managed infrastructure.

> 📖 **Official reference:** [What are Hosted Agents?](https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agents)

---

## What are Hosted Agents?

Hosted agents are a **preview** capability in Foundry Agent Service that lets you:

- Run **custom code** (Python, Node.js, etc.) inside a managed container
- Access **external APIs**, databases, and services from your agent
- Execute **long-running tasks** that go beyond simple prompt-response patterns
- Maintain **full control** over the agent's logic while Foundry handles infrastructure

Unlike Prompt agents (configured via portal) or Workflow agents (visual orchestration), Hosted agents give you **complete code ownership** with Foundry-managed hosting.

---

## Workshop Repository

This lab uses the official Microsoft Hosted Agents Workshop:

👉 **[microsoft/Hosted_Agents_Workshop_Lab](https://github.com/microsoft/Hosted_Agents_Workshop_Lab)**

### Getting Started

1. **Clone the workshop repository:**
   ```bash
   git clone https://github.com/microsoft/Hosted_Agents_Workshop_Lab.git
   cd Hosted_Agents_Workshop_Lab
   ```

2. **Follow the instructions** in the repository's README for:
   - Setting up the development environment
   - Building the hosted agent container
   - Deploying to Foundry Agent Service
   - Testing the hosted agent via the Agents Playground

3. **Return here** after completing the hosted agents lab to continue with [Lab 03 — Workflows with LLM](../lab03/)

---

## Prerequisites

In addition to the [main workshop prerequisites](../../README.md#-prerequisites), you'll need:

- [ ] **Docker** installed (for building the container image)
- [ ] Familiarity with the concepts from **Lab 02 Part A** (function calling) and **Part B** (Agent Service)

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Hosted Agent** | A containerized agent deployed on Foundry-managed infrastructure |
| **Agent Container** | Docker image containing your custom agent code |
| **Agent Service Runtime** | Foundry infrastructure that hosts and scales your container |
| **Custom Tools** | Code-defined tools that your hosted agent can invoke |

---

## Expected Result

- Hosted agent built, deployed, and running on Foundry infrastructure
- Agent accessible and testable via the Agents Playground
- Understanding of the differences between Prompt, Workflow, and Hosted agents

---

## References

- [Hosted Agents Workshop Lab (GitHub)](https://github.com/microsoft/Hosted_Agents_Workshop_Lab)
- [What are Hosted Agents?](https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agents)
- [Microsoft Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/overview)
